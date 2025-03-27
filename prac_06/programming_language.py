class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if this is a dynamic programming language."""
        return self.typing == "Dynamic"
