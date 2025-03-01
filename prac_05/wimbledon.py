"""
Wimbledon
Estimate: 30 minutes
Actual: 15 minutes
"""
import csv

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    data = load_data(FILENAME)



def load_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data

main()