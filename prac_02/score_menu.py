MENU = ("(G)et a valid score (must be 0-100 inclusive)"
        "\n(P)rint result"
        "\n(S)how stars"
        "\n(Q)uit"
        "\n>>>")
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main():
    """A menu program that get a valid score, print the result, and show a number of stars"""
    score = get_valid_score()
    choice = input(MENU)
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Based on your score ({score}), your result is {result}.")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        choice = input(MENU)
    print("Thank you and goodbye!")


def get_valid_score():
    """Get the valid score."""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def show_stars(number_of_stars):
    """Print a number of stars."""
    print("*" * number_of_stars)


def determine_result(score):
    """Determine the result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Pass"
    return "Bad"

main()