"""
Guitars! exercise
Estimated time:
Actual time:
"""
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

    def get_age(self, current_year):
        """Return the age of the Guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Determine if the Guitar is vintage."""
        return self.get_age(current_year) > 50