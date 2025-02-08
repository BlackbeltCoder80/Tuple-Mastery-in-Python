#Tuple Mastery in Python
#Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

#Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
#Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
#The function should format and return a string that lists each itinerary. For example, 
#if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

#"Itinerary 1: Alice - From New York to London
# Itinerary 2: Bob - From Tokyo to San Francisco"
from tabulate import tabulate
#Flight Order 
itinerary_list = [
    {"Itinerary": "Itinerary 1", "Passenger": "Alice", "Origin": "New York", "Destination": "London"},
    {"Itinerary": "Itinerary 2", "Passenger": "Bob", "Origin": "Tokyo", "Destination": "San Francisco"}
]

flight_UI = [["\n Make Your Flight Registration"],
["1. Booke a Flight"],
["2. Flight Itinerary"],
["3. Cancel Flight"]]
#Flight Menu

def flight_menu():
    print(tabulate(flight_UI, tablefmt="grid"))
    
# Flight Registgration (Book Flight)
def book_flight():
    flight_passanger = input("Please enter your full name:")
    flight_origin = input("Please enter your flight origin:")
    flight_destination = input("Please enter your flight destination:")
    if flight_passanger and flight_origin and flight_destination:
        itinerary_list.append({
    "Itinerary": f"Itinerary {len(itinerary_list) + 1}",  
    "Passenger": flight_passanger, 
    "Origin": flight_origin, 
    "Destination": flight_destination
})

# View Itineraries (Flight Itinerary)
def view_itineraries():
    if not itinerary_list:
        print("\nNo flights booked yet.\n")
        print(tabulate(itinerary_list, headers=["Itinerary", "Passenger", "Origin", "Destination"], tablefmt="grid"))

while True:
    flight_menu()
    choice = input("\nSelect an option: ")
    if choice == "1":
        book_flight()
    elif choice == "2":
        view_itineraries()
    elif choice == "3":
        print("\Flight registration closed. Goodbye!\n")
        break
    else:
        print("\nInvalid input! Please enter a number between 1 and 3.")