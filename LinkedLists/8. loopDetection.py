from LinkedList import ListNode

# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop. 

def loopDetection(list):
    s = set()
    curr = list
    
    while curr:
        if curr in s:
            return curr
        else:
            s.add(curr)
        curr = curr.next
        
def loopDetectionFastAndSlow(list):
    slow = list
    fast = list
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        
    if fast == None or fast.next == None:
        return None
    
    slow = list
    
    while slow != fast:
        slow = slow.next
        fast = fast.next 
        
    return fast
  
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n2

res = loopDetectionFastAndSlow(n1)
print(res.data if res else res)

res = loopDetection(n1)
print(res.data if res else res)