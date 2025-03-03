from prac_06.guitar import Guitar
from datetime import datetime


def main():
    """Test the Guitar class methods."""
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 500)

    print(f"{gibson_guitar.name} get_age() - Expected {datetime.now().year - gibson_guitar.year}. Got {gibson_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {datetime.now().year - another_guitar.year}. Got {another_guitar.get_age()}")
    print(f"{gibson_guitar.name} is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()