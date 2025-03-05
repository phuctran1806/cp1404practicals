from prac_06.guitar import Guitar


def main():
    """Create some guitars and display all of their information."""
    guitars = []

    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        add_guitar(guitars, guitar_name, guitar_year, guitar_cost)
        guitar_name = input("\nName: ")
    display_guitars(guitars)


def display_guitars(guitars):
    """Display the all guitars in the list."""
    print("\n... snip ...")
    print("\nThese are my guitars:")
    guitar_name_width = max(len(guitar.name) for guitar in guitars)
    guitar_cost_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
    for number, guitar in enumerate(guitars, 1):
        result_string = f"Guitar {number}:  {guitar.name:>{guitar_name_width}} ({guitar.year}), worth $ {guitar.cost:{guitar_cost_width},.2f}"
        if guitar.is_vintage():
            result_string += " (vintage)"
        print(result_string)


def add_guitar(list_of_guitars, name, year, cost):
    """Add the guitar to a list of guitars."""
    guitar = Guitar(name, year, cost)
    list_of_guitars.append(guitar)
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")


main()
