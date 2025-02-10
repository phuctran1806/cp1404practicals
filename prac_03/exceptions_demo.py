"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- The ValueError will occur when the numerator or the denominator is not input as an integer.
2. When will a ZeroDivisionError occur?
- The ZeroDivisionError will occur when the denominator is input as zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes I can.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("The denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")