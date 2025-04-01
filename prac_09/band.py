class Band:
    def __init__(self, name):
        """Construct a Band object with a name and a collection of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band object."""
        musician_as_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_as_str})"

    def add(self, musician):
        """Add a musician to the collection of musicians."""
        self.musicians.append(musician)