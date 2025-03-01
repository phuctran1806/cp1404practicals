"""
Wimbledon
Estimate: 30 minutes
Actual: 40 minutes
"""
import csv

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Load, process, and display the data."""
    data = load_data(FILENAME)
    champion_to_win_count, champion_countries = process_data(data)
    display_result(champion_to_win_count, champion_countries)

def display_result(champion_to_win_count, champion_countries):
    """Display all the champions with their win count, and the champion countries."""
    print("Wimbledon Champions:")
    for champion, win_count in champion_to_win_count.items():
        print(champion, win_count)

    print(f"\nThere are {len(champion_countries)} countries have won Wimbledon:")
    print(", ".join(champion_countries))

def process_data(data):
    """Store the champions associated with their win count, and the champion countries."""
    champion_to_win_count = {}
    countries = set()
    for row in data:
        champion_to_win_count[row[CHAMPION_INDEX]] = champion_to_win_count.get(row[CHAMPION_INDEX], 0) + 1
        countries.add(row[COUNTRY_INDEX])
    return champion_to_win_count, countries

def load_data(filename):
    """Load data and store each row in a list."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data

main()