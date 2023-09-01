numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)  # [2, 3, 4]

name = "Angela"
new_list = [letter for letter in name]
print(new_list)  # ['A', 'n', 'g', 'e', 'l', 'a']

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)  # ['CAROLINE', 'ELEANOR', 'FREDDIE']
