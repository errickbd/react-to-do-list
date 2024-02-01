

# function to add two numbers together
# gonna take two arguments, the numbers I want to toadd
# going to return the sum
def add_two_numbers(num_a, num_b):
    return num_a + num_b

# User input examples
# name = input("What is your name?")
# print(f"hi {name}")

def get_user_input():
    user_input = input("Enter a number:")
    return int(user_input)

# Lambda functions

def add_one(x):
    return x + 1

# the lambda function version of that is ...
add_two = lambda x : x + 2

this_is_a_lambda_with_no_args = lambda : 4

this_one_has_two = lambda x, y : x + y

print(add_two(7))

def get_multiple_inputs():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    return num1 + num2
