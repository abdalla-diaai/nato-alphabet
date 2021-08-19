import pandas

# TODO 1. Create a dictionary in this format:
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")

# use index to iterate through rows and access row using column names, in this example, using letter, code
nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_exit = True
while nato_exit:
    word = input("Enter a word: ").upper()
    if word == "EXIT":
        nato_exit = False
    else:
        # for letter in word:
        #     print(nato_dict[letter])
        output_list = [nato_dict[letter] for letter in word]
        print(output_list)
