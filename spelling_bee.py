import pandas as pd
import pyperclip

# Step 1: Initialize variables
main = str(input("Main letter: "))  # The main letter that should be in the word
include = str(input("Can include: "))  # Letters that must be included in the words
alphabet = list("abcdefghijklmnopqrstuvwxyz")  # The full alphabet
exclude = [let for let in alphabet if let not in include and let != main]  # Letters to exclude from the words

# Step 2: Read the words from the file (assuming words.txt has one word per line)
try:
    words = pd.read_csv("words.txt", header=None)  # Read the words, assuming no header in the file
    words = words[0].dropna().tolist()  # Drop NaN values, then convert the first column to a list
except FileNotFoundError:
    print("Error: The file 'words.txt' was not found.")
    words = []

# Step 3: Filter words that:
# - contain the main letter (e.g., 'l')
# - are at least 4 letters long
# - do not contain any excluded letters
filtered_words = []
for word in words:
    word = str(word).lower()  # Convert each word to lowercase to handle case sensitivity
    if main in word and len(word) >= 4:  # Check if it contains the main letter and is at least 4 chars
        if not any(letter in word for letter in exclude):  # Check if it contains any excluded letters
            filtered_words.append(word)

for word in filtered_words:
    print(word)