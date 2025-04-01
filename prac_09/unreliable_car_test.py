from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("Toyota Innova", 100, 30)
for i in range(10):
    print(f"Test {i+1}. Distance driven: {my_unreliable_car.drive(10)}")