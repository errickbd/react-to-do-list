# lst_of_nums = [3,7,2,4]

# def sum_the_lst(lst):
#     total = 0
#     step = 0
#     for num in lst_of_nums:
#         total += num
#         step +=1
#     return total, step

# def rec_sum_the_lst(lst, call_stack=0):
#     print(call_stack)
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + rec_sum_the_lst(lst[:-1], call_stack+1)
#                     # if len(lst) == 1:
#                     #     return lst[0]
#                     # return lst[0] + rec_sum_the_lst(lst[1:], call_stack+1)

# print(rec_sum_the_lst(lst_of_nums))

# def count_down(n):
#     if n == 0: # while n > 0:
#         return
#     print(n) # print(n)
#     count_down(n-1) # n -= 1

# count_down(5)

# print the current num in func and stop when it gets to 0

# SIMPLE SEARCH

# def simple_search(lst, target):
#     for i, element in enumerate(lst):
#         if element == target:
#             return i  # Return the index of the target if found
#     return -1  # Return -1 if the target is not in the list


def simple_search(lst, tgt, counter=0):
    if not lst:
        return -1
    if tgt == lst[0]:
        return counter
    return simple_search(lst[1:], tgt, counter + 1)


# print(simple_search([5,4,3,2,1], 9))
# print(bool([]))


## BINARY SEARCH
def binary_search(lst, target):
    steps = 0
    low, high = 0, len(lst) - 1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid, steps  # Return the index and steps taken if found
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps  # Return -1 and steps taken if the target is not in the list

def binary_search_rec(lst, tgt, low, high):
    print(low, high)
    if low > high:
        return -1
    mid = (low + high)//2
    if lst[mid] == tgt:
        return mid
    elif lst[mid] > tgt:
        return binary_search_rec(lst, tgt, low, mid-1)
    else:
        return binary_search_rec(lst, tgt, mid+1, high)


lst = [1,3,5,6,7]
print(binary_search_rec(lst, 100, 0, len(lst)-1))