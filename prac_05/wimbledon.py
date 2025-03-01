"""
Wimbledon
Estimate: 30 minutes
Actual: 15 minutes
"""
import csv

FILENAME = "wimbledon.csv"

def main():
    champion_to_count = retrieve_champion_to_count(FILENAME)

    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(champion, count)

def retrieve_champion_to_count(filename):
    champion_to_count = {}
    with open(filename, "r", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            champion_to_count[row[2]] = champion_to_count.get(row[2], 0) + 1
    return champion_to_count


main()