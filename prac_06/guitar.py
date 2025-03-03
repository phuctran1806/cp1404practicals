"""
Guitars! exercise
Estimated time:
Actual time:
"""
from datetime import datetime

VINTAGE_THRESHOLD = 50

class Guitar:
    """Represents a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the Guitar."""
        return datetime.now().year - self.year

    def is_vintage(self):
        """Determine if the Guitar is vintage."""
        return self.get_age() > VINTAGE_THRESHOLD