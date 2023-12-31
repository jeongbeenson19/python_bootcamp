import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
df = pd.DataFrame(data)

user_input = input("Write a word: ")
user_inputs = [letter.upper() for letter in user_input]

result = []
for letter in user_inputs:
    for (index, row) in df.iterrows():
        if letter in row.iloc[0]:
            letter_with_code = [letter, row.iloc[1]]
            result.append(letter_with_code)

print(result)