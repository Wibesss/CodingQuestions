
# Implement a function to check if a binary tree is balanced. 
# For the purposes of this question, a balanced tree is defined to be a tree such that 
# the heights of the two subtrees of any node never differ by more than one. 

def checkBalancedTree(node):
    if node == None:
        return True
    
    heightDiff = getHeight(node.leftChild) - getHeight(node.rightChild)
    
    if abs(heightDiff) > 1:
        return False
    else:
        return checkBalancedTree(node.leftChild) and checkBalancedTree(node.rightChild)

def getHeight(node):
        if node.leftChild == None and node.leftChild == None:
            return 0
        
        left = getHeight(node.leftChild)
        right = getHeight(node.rightChild)
        return max(right, left) + 1