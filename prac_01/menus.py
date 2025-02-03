MENU = "(H)ello\n(G)oodbye\n(Q)uit\n>>> "

name = input("Enter name: ")
choice = input(MENU).upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    choice = input(MENU).upper()
print("Finished.")