from LinkedList import LinkedList

# You have two numbers represented by a linked list, where each node contains a single digit. 
# The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
# What if the digits are stored in the forward orded

def sumListNumbersReverse(list1, list2):
    num1 = 0
    digit1 = list1.head
    power = 0
    while digit1:
        num1 += pow(10, power) * digit1.data
        power += 1
        digit1 = digit1.next
    
    num2 = 0
    digit2 = list2.head
    power = 0
    while digit2:
        num2 += pow(10, power) * digit2.data
        power += 1
        digit2 = digit2.next
    
    resNum = num1 + num2
    res = LinkedList()
    while resNum > 0:
        digit = resNum % 10
        resNum //= 10
        res.appendNode(digit)
        
    return res

linked_list1 = LinkedList()
linked_list1.appendNode(7)
linked_list1.appendNode(1)
linked_list1.appendNode(6)

linked_list2 = LinkedList()
linked_list2.appendNode(5)
linked_list2.appendNode(9)
linked_list2.appendNode(2)

linked_list1.displayList()
linked_list2.displayList()

res = sumListNumbersReverse(linked_list1, linked_list2)

res.displayList()
        

def sumListNumbersForward(list1, list2):
    num1 = 0
    digit1 = list1.head
    numOfDigits = 0
    
    while digit1.next:
        numOfDigits += 1
        digit1 = digit1.next
    
    
    digit1 = list1.head
        
    while digit1:
        num1 += pow(10, numOfDigits) * digit1.data
        numOfDigits -= 1
        digit1 = digit1.next
    
    num2 = 0
    digit2 = list2.head
    numOfDigits = 0
    
    while digit2.next:
        numOfDigits += 1
        digit2 = digit2.next

    
    digit2 = list2.head
    while digit2:
        num2 += pow(10, numOfDigits) * digit2.data
        numOfDigits -= 1
        digit2 = digit2.next

    
    resNum = num1 + num2
    res = LinkedList()
    while resNum > 0:
        digit = resNum % 10
        resNum //= 10
        res.appendToHead(digit)
        
    return res

print("----------------------------------------------------")
linked_list3 = LinkedList()
linked_list3.appendNode(6)
linked_list3.appendNode(1)
linked_list3.appendNode(7)

linked_list4 = LinkedList()
linked_list4.appendNode(2)
linked_list4.appendNode(9)
linked_list4.appendNode(5)

linked_list3.displayList()
linked_list4.displayList()

res = sumListNumbersForward(linked_list3, linked_list4)

res.displayList()