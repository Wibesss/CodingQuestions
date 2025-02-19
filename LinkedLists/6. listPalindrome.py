from LinkedList import LinkedList

# Implement a function to check if a linked list is a palindrome.

def listPalindrome(list : LinkedList):
    reverseList = LinkedList()
    
    front = list.head
    while front:
        reverseList.appendNode(front.data)
        front = front.next
        
    front = list.head
    back = reverseList.head
    while front and back:
        if front.data != back.data:
            return False
        front = front.next
        back = back.next
    
    return True


linked_list = LinkedList()
linked_list.appendNode(1)
linked_list.appendNode(2)
linked_list.appendNode(3)
linked_list.appendNode(2)
linked_list.appendNode(1)
linked_list.displayList()

print(listPalindrome(linked_list))
