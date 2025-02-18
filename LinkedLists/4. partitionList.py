from LinkedList import LinkedList

# Write code to partition a linked list around a value x, 
# such that all nodes less than x come before all nodes greater than or equal to x. 
# If x is contained within the list, the values of x only need to be after the elements less than x. 
# The partition element x can appear anywhere in the "right partition"
# it does not need to appear between the left and right partitions.

def paritionList(linkedList, val):
    smaller = LinkedList()
    bigger = LinkedList()
    
    curr = linkedList.head
    
    while curr:
        if curr.data >= val:
            bigger.append(curr.data)
        else:
            smaller.append(curr.data)
        curr = curr.next
    
    return smaller.appendList(bigger)
    
    
