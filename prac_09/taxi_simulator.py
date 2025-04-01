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
            choose_taxi(taxis)
        elif option == "d":
            print("Drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        option = input(f"{", ".join(OPTIONS)}\n>>> ").strip().lower()
    print(f"Total trip cost: ${total_trip_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi."""
    print("Taxis available:")
    display_taxis(taxis)
    chosen_index = int(input("Choose taxi: "))
    if chosen_index < 0 or chosen_index >= len(taxis):
        print("Invalid taxi choice")
    else:
        return taxis[chosen_index]



if __name__ == '__main__':
    main()