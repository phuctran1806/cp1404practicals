import random

def main():
    """A program that determine the result from the score."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"Based on your score ({score}), your result is {result}.")

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"From the random score ({random_score}), the random result is {random_result}.")

def determine_result(score):
    """Get the result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Pass"
    return "Bad"

main()