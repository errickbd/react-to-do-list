import file1
import file3 as my_custom_name

# Prefer doing it this way in general
# More explicit, makes it easier to see what other modules/files
# your functions, etc are being used in
from file4 import yet_another_function, not_using_this

print(type(file1))
file1.say_hello()

print(file1.something_important)

my_custom_name.say_goodbye()

yet_another_function()
not_using_this()