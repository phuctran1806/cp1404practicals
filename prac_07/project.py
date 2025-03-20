from datetime import datetime

class Project:
    """Represent a Project object."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Represent a Project object as a string."""
        return f"{self.name}, start: {datetime.strftime(self.start_date, "%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Determine if this project's priority is less than other project's priority."""
        return self.priority < other.priority

