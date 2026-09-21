class Node:
    def __init__(self, data, next=None):
        self.value = data
        self.next = next


# First Linked List
a = Node(16)
b = Node(26)
c = Node(36)
d = Node(46)

a.next = b
b.next = c
c.next = d


# Second Linked List
x1 = Node(29)
x2 = Node(39)
x3 = Node(49)
x4 = Node(59)

x1.next = x2
x2.next = x3
x3.next = x4


# Current pointers
current1 = a
current2 = x1


# Carry
carry = 0


# Dummy node for result list
dummy = Node(0)
tail = dummy


# Addition
while current1 is not None and current2 is not None:

    print(current1.value, "+", current2.value)

    total = current1.value + current2.value + carry

    result_digit = total % 10
    carry = total // 10

    print("TOTAL:", total)
    print("RESULT DIGIT:", result_digit)
    print("CARRY:", carry)

    # New node
    new_node = Node(result_digit)

    # Add new node to result list
    tail.next = new_node
    tail = new_node

    # Move pointers
    current1 = current1.next
    current2 = current2.next


# If carry is remaining
if carry != 0:
    new_node = Node(carry)
    tail.next = new_node
    tail = new_node


# Display result
current = dummy.next

print("\nResult Linked List:")

while current is not None:
    print(current.value, end=" → ")
    current = current.next

print("NONE")