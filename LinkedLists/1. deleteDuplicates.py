from LinkedList import LinkedList

# Write code to remove duplicates from an unsorted linked list.

def deleteDuplicates(linkedList):
    s = set()
    prev = None
    curr = linkedList.head
    while curr:
        if curr.data in s:
            prev.next = curr.next
        else:
            s.add(curr.data)
            prev = curr
        curr = curr.next
        
def deleteDuplicatesNoSet(linkedList):
    curr = linkedList.head
    while curr:
        runner = curr
        while runner.next:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(20)
linked_list.append(30)
linked_list.append(30)
linked_list.display()


deleteDuplicatesNoSet(linked_list)
linked_list.display()
        