"""
Project Management Program
Estimate: 3 hours
Actual:
"""
from datetime import datetime
from project import Project

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
        ">>> ")
DEFAULT_FILE = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    project_objects = load_projects(DEFAULT_FILE)
    load_filename_input = ""

    menu_choice = input(MENU).upper().strip()
    while menu_choice != "Q":
        if menu_choice == "L":
            print("Load")
        elif menu_choice == "S":
            print("Save")
        elif menu_choice == "D":
            print("Display")
        elif menu_choice == "F":
            print("Filter")
        elif menu_choice == "A":
            print("Add")
        elif menu_choice == "U":
            print("Update")
        else:
            print("Invalid choice")
        menu_choice = input(MENU).upper().strip()




def load_projects(filename):
    project_objects = []
    with open(filename) as in_file:
        in_file.readline()  # Skip the header
        for line in in_file:
            parts = line.split("\t")
            project = Project(
                parts[0],
                datetime.strptime(parts[1], "%d/%m/%Y").strftime("%d/%m/%Y"),
                int(parts[2]),
                float(parts[3]),
                int(parts[4]))
            project_objects.append(project)
    print(f"Loaded {len(project_objects)} projects from {filename}")
    return project_objects


if __name__ == "__main__":
    main()
