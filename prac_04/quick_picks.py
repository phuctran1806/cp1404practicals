import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_ROW = 6

number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 0:
    print("Invalid input. Try again.")
    number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_ROW):
        random_number = random.randint(MINIMUM, MAXIMUM)
        while random_number in quick_pick:
            random_number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(random_number)
    quick_pick.sort()
    print(" ".join([f"{number:2}" for number in quick_pick]))