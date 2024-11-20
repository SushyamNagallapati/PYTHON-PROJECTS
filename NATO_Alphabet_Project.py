import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

new_alphabet = {row.letter:row.code for (index, row) in data_frame.iterrows()}

user_guess = input("Enter a name: ").upper()

answer = [new_alphabet[letter] for letter in user_guess]
print(answer)

