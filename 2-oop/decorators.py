"""
Decorates a function to print some extra stuff

Takes a function as an argument, wraps it in another function,
and returns the wrapped function.
"""
def my_decorator(func):
    def func_wrapper():
        print("Do stuff Before we call the function we wrapped")
        func()
        print("Do stuff after we call the function we wrapped")

    return func_wrapper

@my_decorator
def say_goodbye():
    print("Goodbye!")
    return "farewell"


# say_goodbye()
# say_goodbye()
# say_goodbye()

class Person:
    def __init__(self, first_name, last_name, age): 
        self._first_name = first_name.lower()
        self._last_name = last_name.lower()
        self._age = age

        self._email = None

    @property
    def email(self):
        if self._email == None:
            return "No email"

        return self._email

    @email.setter
    def email(self, new_email):
        # Do all validation stuff
        if isinstance(new_email, str):
            self._email = new_email
        else:
            return "Email not valid because not string.." # put stuff here

    def compare_first_name(self, compare_to):
        if compare_to.lower() == self._first_name:
            return True
        
        return False

    


    @property
    def get_first_name(self):
        return self._first_name

    @property
    def get_last_name(self):
        return self._last_name

    @property
    def full_name(self):
        return f"{self._first_name.capitalize()} {self._last_name.capitalize()}"

    @get_first_name.setter
    def set_first_name(self, new_name):
        if isinstance(new_name, str):
            self._first_name = new_name.lower()
        else:
            print("Name must be a string")

alice = Person("alice", "in wonderland", 20)
alice.set_first_name = "BOB"
print(alice.get_first_name)
print(alice.full_name)

print(alice.email)
alice.email = "alice@gmail.com"
print(alice.email)