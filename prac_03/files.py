# 1
name = input("Enter your name: ")
out_file_name = open(f"{name}.txt", "w")
print(name, file=out_file_name)
out_file_name.close()

# 2
in_file_name = open(f"{name}.txt", "r")
in_file_name_content = in_file_name.readline()
print(f"Hi {in_file_name_content.strip()}!")
in_file_name.close()

# 3
total_of_the_first_two_numbers = 0
with open("numbers.txt", "r") as in_file_numbers:
    lines = in_file_numbers.readlines()[:2] # Read only the first two numbers
    for line in lines:
        total_of_the_first_two_numbers += int(line.strip())
print(total_of_the_first_two_numbers)

# 4
total = 0
with open("numbers.txt", "r") as in_file_numbers:
    for line in in_file_numbers:
        total += int(line.strip())
print(total)