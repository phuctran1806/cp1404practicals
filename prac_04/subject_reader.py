"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    print_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def print_data(data):
    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]:12} and has {parts[2]:3} students")

main()