from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

OPTIONS = ["q)uit", "c)hoose taxi", "d)rive"]

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_trip_cost = 0

    print("Let's drive!")
    option = input(f"{", ".join(OPTIONS)}\n>>> ").strip().lower()
    while option != "q":
        if option == "c":
            print("Choose taxi")
        elif option == "d":
            print("Drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        option = input(f"{", ".join(OPTIONS)}\n>>> ").strip().lower()
    print(f"Total trip cost: ${total_trip_cost:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")









if __name__ == '__main__':
    main()