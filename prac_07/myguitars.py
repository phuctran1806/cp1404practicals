from guitar import Guitar

FILENAME = "guitars.csv"
NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)

    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        add_guitar(guitars, guitar_name, guitar_year, guitar_cost)
        guitar_name = input("\nName: ")



def add_guitar(guitars, guitar_name, guitar_year, guitar_cost):
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar)
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)





def load_guitars(filename):
    """Construct Guitar objects from a CSV file and store them in a list."""
    guitars = []
    with open(filename) as infile:
        for line in infile:
            parts = line.split(',')
            parts[YEAR_INDEX] = int(parts[YEAR_INDEX])
            parts[COST_INDEX] = float(parts[COST_INDEX])
            guitar = Guitar(parts[NAME_INDEX], parts[YEAR_INDEX], parts[COST_INDEX])
            guitars.append(guitar)
    return guitars


main()