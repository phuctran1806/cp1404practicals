class Band:
    def __init__(self, name):
        """Construct a Band object with a name and a collection of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the collection of musicians."""
        self.musicians.append(musician)