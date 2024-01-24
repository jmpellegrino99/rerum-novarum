import pandas as pd
import numpy as np
import re
import sqlite3

conn = sqlite3.connect("wordle.db")

df = pd.read_csv("words.csv")

all_5l_words = df["word"].tolist()

def letters_in_common(word1, word2):
    distinct_letters = list(set(word1 + word2))
    return len(set(word1)) + len(set(word2)) - len(distinct_letters)

def avg_matches(test_word):
    counts = []
    to_test = [word for word in all_5l_words if word != test_word]
    for word in to_test:
        counts.append(letters_in_common(test_word, word))
    return np.mean(counts)

#Run to create the average matches dictionary:
# frequencies = []
# for word in all_5l_words:
#     frequencies.append(avg_matches(word))
# freq_df = pd.DataFrame(data={"word": all_5l_words, "match_rate": frequencies})
# freq_df.to_csv("freq_df.csv")

dic = pd.read_csv("freq_df.csv")
dic.to_sql("dic", conn, index=False, if_exists="replace")

no_match_arose = [word for word in all_5l_words if re.match(r"^[^arose]*$", word)]
no_match_arose_dic = pd.DataFrame(data={"word": no_match_arose})
no_match_arose_dic.to_sql("no_match_arose", conn, index=False, if_exists="replace")

query = """
select
*
from dic
where word in (select word from no_match_arose)
order by match_rate desc
;
"""

result = pd.read_sql_query(query, conn)
print(result)