from LinkedList import Node

# Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, 
# given only access to that node.

def deleteMiddleNode(node):
    if not node.next:
        return False
    
    node.data = node.next.data
    node.next = node.next.next
    return True