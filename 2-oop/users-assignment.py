# Make user class
# xfirst name
# xlast name
# x__str__ method
# method for full name
# x email
# drivers license
# date of birth

class User:
    def __init__(
            self, 
            id,
            first_name, 
            last_name, 
            dob,
            email=None, 
            drivers_license=None) -> None:

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.drivers_license = drivers_license

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, born in {self.dob}"

alice = User(0, "Alice", "In Wonderland", "alice@gmail.com", "The 1800s")
louis = User(1, "Louis", "Carrol", "Also The 1800s")

print(alice)
print(alice.get_full_name())