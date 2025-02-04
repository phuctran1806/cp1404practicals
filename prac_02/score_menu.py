from xmlrpc.client import MAXINT

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
            pass
        elif choice == "P":
            pass
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