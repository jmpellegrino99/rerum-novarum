import pandas as pd
import numpy as np
import re
import sqlite3

# conn = sqlite3.connect("wordle.db")
# df.to_sql("df", conn, index=False, if_exists="replace")
# df_result = pd.read_sql_query(query, conn)
# conn.commit()
# conn.close()

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

# dic = pd.read_csv("freq_df.csv")
# print(dic)

#Run to create the average matches dictionary for words that do not overlap with "arose":
# non_starters = [word for word in all_5l_words if bool(re.match(r"^[^arose]*$", word))]
# non_starter_frequencies = []
# for word in non_starters:
#     non_starter_frequencies.append(avg_matches(word))
# freq_df = pd.DataFrame(data={"word": non_starters, "match_rate": non_starter_frequencies})
# freq_df.to_csv("non_starter_freq_df.csv")

non_starter_dic = pd.read_csv("non_starter_freq_df.csv")
non_starter_dic_sorted = non_starter_dic.sort_values(by="match_rate", ascending=False)
print(non_starter_dic_sorted)