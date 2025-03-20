"""
Project Management Program
Estimate: 3 hours
Actual:
"""
from datetime import datetime
from project import Project
from operator import attrgetter

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
        ">>> ")


def main():
    print("Welcome to Pythonic Project Management")

    project_filename = "projects.txt"
    project_objects = load_projects(project_filename)

    menu_choice = input(MENU).upper().strip()
    while menu_choice != "Q":
        if menu_choice == "L":
            project_filename = input("Please enter a filename to load: ")
            try:
                project_objects = load_projects(project_filename)
            except FileNotFoundError:
                print(f"{project_filename} not found.")
        elif menu_choice == "S":
            print("Save")
        elif menu_choice == "D":
            display_projects(project_objects)
        elif menu_choice == "F":
            filter_projects_by_date(project_objects)
        elif menu_choice == "A":
            add_project(project_objects)
        elif menu_choice == "U":
            update_project(project_objects)
        else:
            print("Invalid choice")
        menu_choice = input(MENU).upper().strip()


def load_projects(filename):
    """Load all the projects from a .txt file."""
    project_objects = []
    with open(filename) as in_file:
        in_file.readline()  # Skip the header
        for line in in_file:
            parts = line.split("\t")
            project = Project(
                parts[0],
                datetime.strptime(parts[1], "%d/%m/%Y"),
                int(parts[2]),
                float(parts[3]),
                int(parts[4]))
            project_objects.append(project)
    print(f"Loaded {len(project_objects)} projects from {filename}")
    return project_objects


def display_projects(project_objects):
    """Display all the incomplete and completed projects."""
    incomplete_project_objects = []
    completed_project_objects = []
    for project in project_objects:
        if project.completion_percentage == 100:
            completed_project_objects.append(project)
        else:
            incomplete_project_objects.append(project)

    print("Incomplete projects:")
    for incomplete_project in sorted(incomplete_project_objects, key=attrgetter("priority")):
        print(f"  {incomplete_project}")
    print("Completed projects:")
    for completed_project in sorted(completed_project_objects, key=attrgetter("priority")):
        print(f"  {completed_project}")


def filter_projects_by_date(project_objects):
    """Display all the projects that start after a given date."""
    date = datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y")
    for project in sorted([project for project in project_objects if project.start_date >= date],
                          key=attrgetter("start_date")):
        print(project)


def add_project(project_objects):
    """Add a new project."""
    print("Let's add a new project.")
    name = input("Name: ")
    start_date = datetime.strptime(input("Start date: "), "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    project_objects.append(new_project)


def get_updated_value(temporary_value, prompt):
    """Helper function for update_project() function, which prompt the user for a new value, returning the current value if input is blank."""
    new_value = input(prompt).strip()
    return int(new_value) if new_value else temporary_value


def update_project(project_objects):
    """Update a project."""
    # Display all the projects with numbers.
    for i, project in enumerate(project_objects):
        print(f"{i} {project}")

    chosen_project = project_objects[int(input("Project choice: "))]
    print(chosen_project)

    chosen_project.completion_percentage = get_updated_value(chosen_project.completion_percentage, "New Percentage: ")
    chosen_project.priority = get_updated_value(chosen_project.priority, "New Priority: ")


if __name__ == "__main__":
    main()
