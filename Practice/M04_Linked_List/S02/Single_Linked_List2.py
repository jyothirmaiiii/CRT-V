'''
Singly linked List :
Algorithm
1. create Node
2. Inserr the data into the nodes
3. Generate the connection btw the nodes
4. traverse all the nodes
'''
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

def traverse():
    curr = node1
    while curr:
        print(curr.data,end = " -> ")
        curr = curr.next
    print("Node")

traverse()

'''

# Insertion at the begining in singly linked list:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def traverse(head):
    curr = head
    while curr:
        print(curr.data,end = " -> ")
        curr = curr.next
    print("None")

head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)

print("Insertion at the begin")
traverse(head)

        