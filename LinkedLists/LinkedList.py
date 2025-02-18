
class ListNode:
    def __init__(self, data):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def appendNode(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def appendList(self, other_list):
        if not self.head:
            self.head = other_list.head
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = other_list.head 


    def displayList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def deleteNode(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if not current:
            print(f"Node with data {data} not found!")
            return
        
        prev.next = current.next
        current = None


