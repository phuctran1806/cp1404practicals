from guitar import Guitar
import csv

FILENAME = "guitars.csv"
NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        add_guitar(guitars, guitar_name, guitar_year, guitar_cost)
        guitar_name = input("\nName: ")
    save_guitars(FILENAME, guitars)


def add_guitar(guitars, guitar_name, guitar_year, guitar_cost):
    """Add a new guitar to the list of guitars."""
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar)
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")


def load_guitars(filename):
    """Construct Guitar objects from a CSV file and store them in a list."""
    guitars = []
    with open(filename) as in_file:
        for line in in_file:
            parts = line.split(',')
            parts[YEAR_INDEX] = int(parts[YEAR_INDEX])
            parts[COST_INDEX] = float(parts[COST_INDEX])
            guitar = Guitar(parts[NAME_INDEX], parts[YEAR_INDEX], parts[COST_INDEX])
            guitars.append(guitar)
    return guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    print(type(guitars))
    with open(filename, 'w', newline="") as out_file:
        csvwriter = csv.writer(out_file)
        for guitar in guitars:
            csvwriter.writerow([guitar.name, guitar.year, guitar.cost])



main()