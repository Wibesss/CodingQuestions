from LinkedList import LinkedList

# Write code to partition a linked list around a value x, 
# such that all nodes less than x come before all nodes greater than or equal to x. 
# If x is contained within the list, the values of x only need to be after the elements less than x. 
# The partition element x can appear anywhere in the "right partition"
# it does not need to appear between the left and right partitions.

def paritionList(linkedList, val):
    if not linkedList.head or not linkedList.head.next:
        return linkedList

    smaller = LinkedList()
    bigger = LinkedList()
    
    curr = linkedList.head
    
    while curr:
        if curr.data < val:
            smaller.appendNode(curr.data)
        else:
            bigger.appendNode(curr.data)
        curr = curr.next
    
    if not smaller.head:
        return bigger
    
    last = smaller.head
    while last.next:
        last = last.next
    
    last.next = bigger.head

    return smaller

linked_list = LinkedList()
linked_list.appendNode(25)
linked_list.appendNode(30)
linked_list.appendNode(35)
linked_list.appendNode(10)
linked_list.appendNode(15)
linked_list.appendNode(20)

linked_list.displayList()

linked_list = paritionList(linked_list, 20)

linked_list.displayList()
