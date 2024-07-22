import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import random
from scipy.stats import rankdata

num_only_checking = 79381
num_only_mortgage = 21117
num_checking_and_mortgage = 21242
num_checking = num_only_checking + num_checking_and_mortgage
num_mortgage = num_only_mortgage + num_checking_and_mortgage

poss_start = 10**11
poss_end = 10**12 - 1

all_cust_id_int = list(random.sample(range(poss_start, poss_end + 1), num_only_checking + num_only_mortgage + num_checking_and_mortgage))

all_cust_id = [
    "0000" + str(item)
    for item in all_cust_id_int
]

only_checking_cust_id = all_cust_id[0:num_only_checking]
checking_and_mortgage_cust_id = all_cust_id[num_only_checking:(num_only_checking+num_checking_and_mortgage)]
only_mortgage_cust_id = all_cust_id[(num_only_checking+num_checking_and_mortgage):]
checking_cust_id = only_checking_cust_id + checking_and_mortgage_cust_id
mortgage_cust_id = only_mortgage_cust_id + checking_and_mortgage_cust_id

# Checking balances
checking = np.random.exponential(scale=2500, size=num_checking)

# Checking ranks
checking_ranks = rankdata(checking, method='average')

# State assignment
states = ['OH', 'NY', 'PA', 'WA', 'CO', 'Other']
state = []
for rank in checking_ranks:
    state_probabilities = [0.3, 0.35, 0.1 - (rank / num_checking) / 25, 0.07 + (rank / num_checking) / 50,
                           0.05 + (rank / num_checking) / 50, 0.13]
    state.append(np.random.choice(states, p=state_probabilities))

# Primacy assignment
primacy = [
    np.random.rand() < rank / num_checking for rank in checking_ranks
]

# Savings balances, correlated with checking balance
savings = []
for checking_bal in checking:
    classifier = np.random.rand()
    if classifier < 0.3:
        savings.append(None)
    else:
        savings.append(round(max(
            np.random.normal(loc=0.5 * checking_bal, scale=0.05 * checking_bal) + 10000*(np.random.rand() - 0.5)
            , 10),2)
        )

# Print summary statistics
print("min cust id: ", np.min([int(item) for item in checking_cust_id]))
print("max cust id: ", np.max([int(item) for item in checking_cust_id]))
print("max checking: ", round(np.max(checking),2))
print("min checking: ", round(np.min(checking),2))

# Handle None values in savings before calculating max/min
savings_cleaned = [s for s in savings if s is not None]
if savings_cleaned:
    print("max savings: ", round(np.max(savings_cleaned),2))
    print("min savings: ", round(np.min(savings_cleaned),2))
else:
    print("No valid savings data")

print("min checking rank: ", np.min(checking_ranks))
print("max checking rank: ", np.max(checking_ranks))
print("sum of primacy: ", sum(primacy))
print("unique # of acct nos: ", len(set(checking_cust_id)))
print("sum of checking bals: ", round(np.sum(checking),0))
if savings_cleaned:
    print("sum of savings bals: ", round(np.sum(savings_cleaned),2))
else:
    print("No valid savings data")

if len(set(checking_cust_id)) == num_only_checking + num_checking_and_mortgage:
    print("All account numbers are unique.")
else:
    print("There is at least one account number duplicate.")

# Create checking DataFrame
df = pd.DataFrame(data={
    "cust_id": checking_cust_id,
    "state": state,
    "checking": [round(item,2) for item in checking],
    "savings": savings,
    "primacy": primacy
})

# Print state value counts and unique states
print(df["state"].value_counts())
print("unique list of states: ", list(set(str(st) for st in state)))
print("\n")
print("checking/savings corr: ", round(df['checking'].corr(df['savings']),2))
print("\nchecking/primacy corr: ", round(df['checking'].corr(df['primacy']),2))
print("\nsavings/primacy corr: ", round(df['savings'].corr(df['primacy']),2))
print("\n")

# Save DataFrame to CSV
df.to_csv('checking.csv', index=False)

# Set up a SQL connection
conn = sqlite3.connect('sql_training_data.db')

df.to_sql('checking', conn, if_exists='replace', index=False)

# Start creating mortgage data for the second dataset
mortgage_terms = [10,15,20,30]
mortgage_probs = [0.05,0.20,0.05,0.70]
mortgage_actual_terms = []

for item in mortgage_cust_id:
    mortgage_actual_terms.append(np.random.choice(mortgage_terms, p=mortgage_probs))

mortgage_amount = np.random.normal(loc=375000, scale=75000, size = len(mortgage_cust_id))

# Start working on mortgage dataframe:
mo1 = pd.DataFrame(data={
    "cust_id": mortgage_cust_id,
    "term": mortgage_actual_terms,
    "amount": mortgage_amount
    }
)

mo1.to_sql('mortgage1', conn, if_exists='replace', index=False)

query = """
select
m.cust_id
, m.term
, m.amount
, case when c.primacy is null then 0 else c.primacy end as primacy
, c.state
from mortgage1 m
left join checking c
    on m.cust_id = c.cust_id
"""

mo2 = pd.read_sql_query(query,conn)

prim = mo2['primacy'].tolist()

apy = []

for item in prim:
    if item == 1:
        apy.append(np.random.normal(loc=3.5, scale=0.5))
    else:
        apy.append(np.random.normal(loc=4.25, scale=0.5))

mo3 = pd.DataFrame(data={
    "cust_id": mortgage_cust_id,
    "term": [int(item) for item in mortgage_actual_terms],
    "amount": [int(item) for item in mortgage_amount],
    "apy": [round(max(item,2),2) for item in apy]
    }
)

mo3.to_csv('mortgage.csv',index=False)

conn.close()