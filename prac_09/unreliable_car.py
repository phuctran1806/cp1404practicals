from prac_09.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar object."""
        super().__init__(name, fuel)
        self.reliability = max(0, min(100, reliability))  # Clamps percentage value between 0 and 100

