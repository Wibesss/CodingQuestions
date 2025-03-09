
# Write an algorithm to find the "next" node of a given node in a binary search tree. 
# You may assume that each node has a link to its parent. 

def findNextNode(node):
    if node is None or node.rightChild is None:
        return None
    
    res = node.rightChild
    
    while res.leftChild:
        res = res.leftChild
        
    return res