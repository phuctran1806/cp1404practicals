name = input("Enter your name: ")
out_file = open(f"{name}.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open(f"{name}.txt", "r")
in_file_name = in_file.readline()
print(f"Hi {in_file_name.strip()}!")
in_file.close()