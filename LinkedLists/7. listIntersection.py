from LinkedList import ListNode

# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. 
# Note that the intersection is defined based on reference, not value. 
# That is, if the kth node of the first linked list is the exact same node (by reference) 
# as the jth node of the second linked list, then they are intersecting.

def listIntersection(node1, node2):
    if node1 == None and node2 == None:
        return None

    tail1, size1 = getTailandSize(node1)
    tail2, size2 = getTailandSize(node2)
    
    if tail1 != tail2:
        return None
    
    bigger = None
    smaller = None
    
    if size1 > size2:
        bigger = node1
        smaller = node2
    else:
        bigger = node2
        smaller = node1
        
    for _ in range(abs(size1-size2)):
        bigger = bigger.next
    
    while bigger != smaller:
        bigger = bigger.next 
        smaller = smaller.next
    
    return bigger


def getTailandSize(node):
    if node == None:
        return None, 0
    
    size = 0
    curr = node
    last = None
    
    while curr:
        size += 1
        last = curr
        curr = curr.next
        
    return last, size
        
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(0)
n6 = ListNode(1)

n1.next = n2
n2.next = n3
n3.next = n4
n5.next = n6
n6.next = n2

res = listIntersection(n1,n5)

print(res.data if res else res)



