import random
from prac_09.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar object."""
        super().__init__(name, fuel)
        self.reliability = max(0, min(100, reliability))  # Clamps percentage value between 0 and 100

    def drive(self, distance):
        """Drive the car with a given distance if the random number is less than the car's reliability."""
        random_number = random.randint(0, 100)
        return super().drive(distance) if random_number < self.reliability else 0