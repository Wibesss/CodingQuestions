from LinkedList import LinkedList

# Implement an algorithm to find the kth to last element of a singly linked list.

def getKthLast(linkedList, k):
    curr = linkedList.head
    runner = linkedList.head
    for _ in range(k):
        if runner != None:
            runner = runner.next
        else:
            return "No K nodes in the list"
    while runner:
        curr = curr.next
        runner = runner.next
    return curr.data

linked_list = LinkedList()
linked_list.appendNode(10)
linked_list.appendNode(20)
linked_list.appendNode(20)
linked_list.appendNode(30)
linked_list.appendNode(30)
linked_list.displayList()

print(getKthLast(linked_list, 5))