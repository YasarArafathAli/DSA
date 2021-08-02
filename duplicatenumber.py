# def dupNumsor(arr):
    
#     a = sorted(arr)
#     for i,v in enumerate(a):
#         if a[i] == a[i + 1]:
#             return v


# def dupNumfreq(arr):
#     n = len(arr)
#     freq = [0] * n
#     for i in arr:
#         freq[i] += 1
#         if freq[i] > 1: 
#             return i

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third




print(dupNum([0,1,2,3,4,3]))
