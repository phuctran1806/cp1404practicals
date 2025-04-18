"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report of incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    income_width = max((len(str(income)) for income in incomes))
    for month, income in enumerate(incomes):
        total += income
        print(f"Month {month:2} - Income: $   {income:{income_width}.2f}         Total: $   {total:{len(str(total))}.2f}")


main()