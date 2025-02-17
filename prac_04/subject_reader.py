"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load and display data."""
    data = load_data()
    print_data(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data

def print_data(data):
    """Display subject details."""
    lecturer_width = max((len(parts[1]) for parts in data))
    number_of_students_width = max((len(str(parts[2])) for parts in data))

    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]:{lecturer_width}} and has {parts[2]:{number_of_students_width}} students")

main()