from LinkedList import LinkedList, Node

def deleteDuplicates(list):
    s = set()
    
    prev = None
    curr = list.head
    while curr.next:
        if curr.data in s:
            prev.next = curr.next
            curr.data = None
        
        s.add(curr.data)
        curr = curr.next
        
        