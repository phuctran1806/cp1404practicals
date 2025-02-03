"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

display menu
get choice
while choice != Q
    if choice == C
        get celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        print fahrenheit
    else if choice == F
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        print celsius
    else
        display invalid message
    display menu
    get choice
display finished message
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")