def linear_search(tgt, lst):
    steps = 0
    for num in lst:
        steps += 1
        if num == tgt:
            return f"STEPS: {steps} ANSWER: {num}"


def binary_search(tgt, lst):
    steps = 0
    left = 0
    right = len(lst)-1
    while left <= right:
        steps +=1 # increase step to show how many times this is repeated
        middle = (left + right)//2
        if lst[middle] == tgt:
            return f"STEPS: {steps} ANSWER: {tgt}"
        elif lst[middle] < tgt:
            left = middle + 1
        else:
            right = middle - 1
    return f"STEPS: {steps} ANSWER: {-1}"


list_of_numbers = ['2','1',"Francisco", "Adam", "Nick", "Tyler", "Tristan", "Will", "Neka"]
print(sorted(list_of_numbers))
target = "Nick"

# print(linear_search(target, sorted(list_of_numbers)))
# print(binary_search(target, sorted(list_of_numbers)))