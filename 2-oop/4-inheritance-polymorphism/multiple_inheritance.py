class Mother:
    def __init__(self):
        self.first_name = "Alice"
        self.favorite_book = "Alice in Wonderland"

class Father:
    def __init__(self):
        self.first_name = "Bob"
        self.favorite_movie = "Star Wars"


class Child(Mother, Father):
    def __init__(self, favorite_play):
        Father.__init__(self)
        Mother.__init__(self)
        self.favorite_play = favorite_play

    def __str__(self):
        return f"""
            First Name: {self.first_name} 
            Favorite Book: {self.favorite_book}
            Favorite Movie: {self.favorite_movie}
            Favorite Play: {self.favorite_play}
        """

carol = Child("Waiting for Godot")
print(carol)