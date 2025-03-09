
# Implement a function to check if a binary tree is a binary search tree. 

def isBSTUtil(root, minValue, maxValue):
    if root is None:
        return True
    
    if not (minValue < root.data < maxValue):
        return False

    return (isBSTUtil(root.leftChild, minValue, root.data) and
            isBSTUtil(root.rightChild, root.data, maxValue))

def isBST(root):
    if root is None:
        return "Tree not found"
    return isBSTUtil(root, float('-inf'), float('inf'))