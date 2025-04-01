from prac_09.unreliable_car import UnreliableCar

reliable_car = UnreliableCar("Reliable Car", 100, 95)
unreliable_car = UnreliableCar("Unreliable Car", 100, 30)

for i in range(1, 11):
    print(f"Test {i+1}:")
    print(f"{reliable_car.name} drove {reliable_car.drive(i)}km")
    print(f"{unreliable_car.name} drove {unreliable_car.drive(i)}km")

print("\nFinal state of each car after testing:")
print(reliable_car)
print(unreliable_car)