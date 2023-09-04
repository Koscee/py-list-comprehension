import pandas

nato_alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from nato_phonetic_alphabet.csv
nato_phonetic_dict = {row.letter: row.code for (_index, row) in nato_alphabet_df.iterrows()}
print(nato_phonetic_dict)


# Create a list of the phonetic code words from a word that user inputs
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()