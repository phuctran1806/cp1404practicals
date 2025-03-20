"""
Project Management Program
Estimate: 3 hours
Actual:
"""
from datetime import datetime
from operator import attrgetter
from project import Project

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
        ">>> ")
PROJECT_HEADERS = [
    "Name\t",
    "Start Date\t",
    "Priority\t",
    "Cost Estimate\t",
    "Completion Percentage\n"
]
DEFAULT_FILENAME = "projects.txt"
ACCEPTING_PROMPTS = ["Y", "Yes"]


def main():
    """A project management program."""
    print("Welcome to Pythonic Project Management")
    project_objects = load_projects(DEFAULT_FILENAME)

    menu_choice = input(MENU).upper().strip()
    while menu_choice != "Q":
        if menu_choice == "L":
            load_project_filename = f"{get_valid_string("Please enter a filename to load: ")}.txt"
            try:
                project_objects = load_projects(load_project_filename)
            except FileNotFoundError:
                print(f"{load_project_filename} not found.")
        elif menu_choice == "S":
            save_project_filename = f"{get_valid_string("Please enter a filename to save: ")}.txt"
            save_projects(save_project_filename, project_objects)
        elif menu_choice == "D":
            incomplete_project_objects = [project for project in project_objects if not project.is_completed()]
            completed_project_objects = [project for project in project_objects if project.is_completed()]
            display_projects(incomplete_project_objects, "Incomplete Projects:")
            display_projects(completed_project_objects, "Completed Projects:")
        elif menu_choice == "F":
            filter_projects_by_date(project_objects)
        elif menu_choice == "A":
            add_project(project_objects)
        elif menu_choice == "U":
            update_project(project_objects)
        else:
            print("Invalid choice")
        menu_choice = input(MENU).upper().strip()

    default_file_saving_choice = get_valid_string(f"Would you like to save to {DEFAULT_FILENAME}? ").title().strip()
    if default_file_saving_choice in ACCEPTING_PROMPTS:
        save_projects(DEFAULT_FILENAME, project_objects)
    print("Thank you using custom-built project management software.")


def load_projects(filename):
    """Load all the projects from a .txt file."""
    project_objects = []
    with open(filename, encoding="utf-8") as in_file:
        in_file.readline()  # Skip the header
        for line in in_file:
            parts = line.split("\t")
            project = Project(
                parts[0],  # Name
                datetime.strptime(parts[1], "%d/%m/%Y"),  # Start Date
                int(parts[2]),  # Priority
                float(parts[3]),  # Cost Estimate
                int(parts[4]))  # Completion Percentage
            project_objects.append(project)
    print(f"Loaded {len(project_objects)} projects from {filename}")
    return project_objects


def save_projects(filename, project_objects):
    """Prompt the user for a filename and save the projects to that file in .txt."""
    with open(filename, "w", encoding="utf-8") as out_file:
        out_file.writelines(PROJECT_HEADERS)  # Add the headers in the file.
        for project in project_objects:
            out_file.write(f"{project.name}\t"
                           f"{datetime.strftime(project.start_date, "%d/%m/%Y")}\t"
                           f"{project.priority}\t"
                           f"{project.cost_estimate:.1f}\t"
                           f"{project.completion_percentage}\n")


def display_projects(projects, heading=""):
    """Display the projects."""
    print(heading)
    for project in sorted(projects):
        print(f"  {project}")


def filter_projects_by_date(project_objects):
    """Display all the projects that start after a given date."""
    date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    for project in sorted([project for project in project_objects if project.start_date >= date],
                          key=attrgetter("start_date")):
        print(project)


def add_project(project_objects):
    """Add a new project."""
    print("Let's add a new project.")
    name = get_valid_string("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ", 0, float('inf'), int)
    cost_estimate = get_valid_number("Cost estimate: $", 0, float('inf'), float)
    completion_percentage = get_valid_number("Percent complete: ", 0, 100, int)
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    project_objects.append(new_project)


def update_project(project_objects):
    """Update a project."""
    # Display all the projects with numbers.
    for i, project in enumerate(project_objects):
        print(f"{i} {project}")

    # User choose a project and update its Completion Percentage and Priority.
    chosen_project = project_objects[int(input("Project choice: "))]
    print(chosen_project)
    for attribute in ["completion_percentage", "priority"]:
        new_value = input(f"New {attribute.replace('_', ' ').title()}: ").strip()
        if new_value:
            setattr(chosen_project, attribute, int(new_value))


def get_valid_number(prompt, minimum, maximum, number_type):
    """Prompt the user for a valid number."""
    while True:
        try:
            input_number = number_type(input(prompt).strip())
            if input_number < minimum or input_number > maximum:
                print("Invalid number")
            else:
                return input_number
        except ValueError:
            print("Invalid number")


def get_valid_date(prompt):
    """Prompt the user for a valid start date."""
    while True:
        try:
            start_date = datetime.strptime(input(prompt), "%d/%m/%Y")
            return start_date
        except ValueError:
            print("Invalid start date")


def get_valid_string(prompt):
    """Prompt the user for a valid string."""
    input_string = input(prompt).strip()
    while not input_string:
        print("Input cannot be blank.")
        input_string = input(prompt).strip()
    return input_string


if __name__ == "__main__":
    main()
