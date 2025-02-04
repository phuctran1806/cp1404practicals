from score import determine_result

MENU = ("(G)et a valid score (must be 0-100 inclusive)"
        "\n(P)rint result"
        "\n(S)how stars"
        "\n(Q)uit"
        "\n>>>")
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main():
    choice = input(MENU)
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Based on your score ({score}), your result is {result}.")
        elif choice == "S":
            pass
        else:
            print("Invalid choice")
        choice = input(MENU)


def get_valid_score():
    """Get the valid score."""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


main()