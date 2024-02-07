class CarManager:
    total_cars = 0
    all_cars = []

    # NOTE: This does not have to be a static method, it would work fine as
    # a normal instance method, but, since this method's behavior involves
    # nothing specific to any particular instance of CarManager, it makes sense
    # for readability and for organizing code for it to be a static method.
    @staticmethod
    def get_car_in_all_cars(car_id):
        # There is probably a more elegant way to do this in python
        for car in CarManager.all_cars:
            if car._id == car_id:
                return car

        # Car does not exist in list, return none
        return None

    def __init__(self, make=None, model=None, year=None, mileage=None, services=[]):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services

        self._id = CarManager.total_cars
        CarManager.total_cars += 1

        CarManager.all_cars.append(self)

    def __str__(self):
        return f" THis lovely car is blah blah ID {self._id} | Make {self._make} | Model {self._model}"

    def __repr__(self):
        return f"ID {self._id} | Make {self._make} | Model {self._model}"