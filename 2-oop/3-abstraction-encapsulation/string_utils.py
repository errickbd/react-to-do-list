class StringUtils:
    @staticmethod
    def is_palindrome(text):
        clean_text = text.replace(" ", "").lower()
        # palindrome: "racecar"
        # reversing a string and comparing original to reverse is how to test for palindrome
        return clean_text == clean_text[::-1]

    @staticmethod
    def add_exclamations(text):
        return f"{text}!!! Wow!"