import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_ROW = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    for j in range(NUMBERS_PER_ROW):
        random_number = random.randint(MINIMUM, MAXIMUM)
        print(f"{random_number:2}", end=" ")
    print()