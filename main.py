import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet_dict = {row['letter']:row['code'] for (index, row) in dataframe.iterrows()}
# print(nato_alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type the word (no spaces or non-alphabetic chars): ")
# print(user_input)

phonetic_words_list = []
for c in user_input:
    phonetic_words_list.append(nato_alphabet_dict.get(c.upper()))
print(phonetic_words_list)
