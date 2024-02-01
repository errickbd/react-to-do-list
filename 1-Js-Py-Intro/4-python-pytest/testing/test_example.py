from example import add_two_numbers, get_user_input, get_multiple_inputs

def test_add_two_numbers():
    # Edge cases
    assert add_two_numbers(2,2) == 4


    # Normal cases
    assert add_two_numbers(3,2) == 5
    assert add_two_numbers(3, -5) == -2
    assert add_two_numbers(-3, -5) == -8
    assert add_two_numbers(0, 0) == 0
    assert add_two_numbers(3, 0) == 3

def examples_of_assertions():
    # equality assertion
    assert "hello" == "Hello" # false
    assert "hello" == "hello" # true
    assert False == 0 # false

    # inequality or not equals assertions
    assert "hello" != "Hello" # true
    assert False != 0 # true

    assertEqual(3,3)
    hi = "hello world"
    assertEqual(hi, "hello world")

    with assertRaises(ZeroDivisionError):
        result = 1 / 0

    assert "apple" in ["apple", "banana", "cherry"]
    assert "strawberry" not in ["apple", "banana", "cherry"]

    assert "hello world".startswith("he")
    assert "hello world".endswith("world")

    assert len([1,4,5]) == 3
    my_list = [3,9, 1]
    assert sorted(my_list) == [1,3,9]

    # Monkey Patching and Testing
    # Especially for programs that take user input


def test_get_user_input(monkeypatch):
    # Simulate user input

    # The same as above but with a lambda function
    monkeypatch.setattr("builtins.input", lambda _ : "42")

    result = get_user_input()

    assert result == 42

def test_get_multiple_inputs(monkeypatch):
    user_inputs = ["5", "7"]
    input_values = iter(user_inputs)

    monkeypatch.setattr("builtins.input", lambda _ : next(input_values))

    result = get_multiple_inputs()

    assert result == 5 + 7