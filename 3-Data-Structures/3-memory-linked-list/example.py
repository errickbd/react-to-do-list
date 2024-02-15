# import sys

# # lst_of_nums = [1,2,3,4,5]
# # print(hex(id(lst_of_nums)))
# # lst_of_nums = lst_of_nums + [6,7]
# # lst_of_nums.append(6)
# # print(lst_of_nums) # [1,2,3,4,5,6,6,7]
# # print(hex(id(lst_of_nums_2)))
# # tpl_of_nums = (1,2,3,4,5)
# # [range(10)]
# # print(sys.getsizeof(lst_of_nums))
# # print(sys.getsizeof(tpl_of_nums))

# def greeting():
#     return "HEllo"

# result = []
# for x in range(100):
#     # print(hex(id(result)))
#     # print(sys.getsizeof(result))
#     result.append(greeting())

# efficient_result = [greeting() for x in range(100)]


# print(f"first result:   {sys.getsizeof(result)}")
# # print(f"second result:  {sys.getsizeof(efficient_result)}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)

# node1.next = node2
# node2.next = node3
# node3.next = node5

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_node):
        current_head = self.head
        self.head = new_node
        new_node.next = current_head

    def insert_at_end(self, ending_node):
        original_head = self.head
        if not self.head:
            self.head = ending_node
            return
        while self.head.next:
            self.head = self.head.next
        self.head.next = ending_node
        self.head = original_head

    def traversing(self):
        original_head = self.head
        while self.head:
            print(self.head, self.head.next)
            self.head = self.head.next
        self.head = original_head

    def delete_by_value(self, key):
        original_head = self.head
        while self.head.next:
            next_node = self.head.next
            if self.head.data == key:
                self.head = next_node
                if key != original_head.data:
                    self.head = original_head
                return
            if next_node.data == key:
                self.head.next = next_node.next
                self.head = original_head
                return
            self.head = next_node


# Link List Starts
lnk_lst_of_nums = LinkedList()
# lnk_lst_of_nums.head = node1
# node0 = Node(0)
# node6 = Node(6)
# # print(lnk_lst_of_nums.head)
# lnk_lst_of_nums.insert_at_beginning(node0)
# lnk_lst_of_nums.insert_at_end(node6)
# lnk_lst_of_nums.traversing()
# lnk_lst_of_nums.delete_by_value(2)
lnk_lst_of_nums.traversing()
[lnk_lst_of_nums.insert_at_end(Node(num)) for num in range(1,11)]
lnk_lst_of_nums.traversing()
lnk_lst_of_nums.delete_by_value(3)
lnk_lst_of_nums.traversing()
