class CarManager:
    total_cars = 0
    all_cars = []

    def __init__(self, make, model, services=[]): 
        # Update total_cars and create id for this car
        self._id = CarManager.total_cars
        CarManager.total_cars += 1
        self._make = make
        self._model = model
        self._services = services

        # Update all_cars
        CarManager.all_cars.append(self)

    def __str__(self):
        return f"ID {self._id} | Make {self._make} | Model {self._model}" 

    def __repr__(self):
        return str(self)

    def add_services(self, new_service):
        self._services.append(new_service)


print("total cars: " + str(CarManager.total_cars))
print("car1")
car1 = CarManager("Jeep", "Wrangler", ['oil change', 'new tires'])
print(car1._id)
print(CarManager.all_cars)

print("total cars: " + str(CarManager.total_cars))
print("car2")
car2 = CarManager("Honda", "Civic", [])
print(car2._id)
print(CarManager.all_cars)

print("total cars: " + str(CarManager.total_cars))
print("car3")
car3 = CarManager("Volkswagen", "Jetta", [])
print(car3._id)
print(CarManager.all_cars)

print("total cars: " + str(CarManager.total_cars))
print("car4")
car4 = CarManager("Chevrolet", "Silverado")
print(car4._id)
print(CarManager.all_cars)