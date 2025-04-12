from prac_09.silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
print(silver_service_taxi)  # Test the __str__() method.

# Test the get_fare() method after an 18-km trip.
silver_service_taxi.drive(18)
assert silver_service_taxi.get_fare() == 48.80