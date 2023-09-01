with open("file1.txt") as file1:
    file1_content = file1.read().splitlines()

with open("file2.txt") as file2:
    file2_content = file2.read().splitlines()

result = [int(num) for num in file1_content if num in file2_content]

print(result)
