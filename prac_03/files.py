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
total = 0
with open("numbers.txt", "r") as in_file_numbers:
    lines = in_file_numbers.readlines()[:2]
    for line in lines:
        total += int(line.strip())
print(total)