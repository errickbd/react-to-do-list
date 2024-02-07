"""
Features:

- Get user input from the command line
    - Welcome / Main menu
        - View all cars
            - Pretty easy: `print(CarManager.all_cars)`
        - View total cars
            - Easy: `print(CarManager.total_cars)`
        - Add a car
            - Get user input for make, model, etc.
                - How to do this? All in one input? Multiple?
        - See car details
            - Get user input for car id we want details for
        - Service a car
            - Get user input for services we want to add
                - Give user list of available services
                    - Get selected service
        - Update Mileage
            - Get user input for ....
                - New total value
        - Quit

X- CarManager     
    X- Create a car that has all the necessary details
        - ALMOST DONE.
    X - Add a car to a list of all cars
    X - Get the list of all cars
    X - Keep a count of the total number of cars
    X - Get the total number of cars
"""

from car_manager import CarManager

def display_view_car_details():
    prompt_message = "Enter ID of Vehicle you want details for:"

    is_valid_input = False

    while(is_valid_input is False):
        # TODO: Wrap the cast in a try/except for error handling
        car_id = int(input(prompt_message))
        print(f"User input {car_id}")

        if car_id is not None:
            is_valid_input = True
            print(CarManager.get_car_in_all_cars(car_id))
        else:
            print("Car ID does not exist")


def display_welcome_menu():
    prompt_message = """
----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
"""

    valid_inputs = ["1", "2", "3", "4", "5", "6", "7"]
    is_valid_input = False

    while(is_valid_input is False):
        user_input = input(prompt_message)
        print(f"User input {user_input}")
        if user_input in valid_inputs:
            is_valid_input = True

            if user_input is "1":
                pass # Replace this with actual code
            if user_input is "2":
                pass # Replace this with actual code
            if user_input is "3":
                pass # Replace this with actual code
            if user_input is "4":
                display_view_car_details()
            if user_input is "5":
                pass # Replace this with actual code
            if user_input is "6":
                pass # Replace this with actual code
            if user_input is "7":
                pass # Replace this with actual code

            
        else:
            print("Invalid menu choice.")

display_welcome_menu()

# Test code
car1 = CarManager("Honda", "Civic")
# print(car1)
# print(CarManager.all_cars)
# print(CarManager.total_cars)

car2 = CarManager("Ford", "Fusion")
# print(car2)
# print(CarManager.all_cars)
# print(CarManager.total_cars)

car3 = CarManager("Toyota", "Prius")

# Testing  get_car_in_all_cars
# print(CarManager.get_car_in_all_cars(1))
