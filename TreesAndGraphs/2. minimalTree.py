from Tree import TreeNode, Tree

# Given a sorted (increasing order) array with unique integer elements, 
# write an algorithm to create a binary search tree with minimal height. 

def minimaltTree(list):
    tree = Tree()
    tree.root = createMinimalTree(list, 0, len(list) - 1)
    return tree

def createMinimalTree(list, start, end):
    if(end < start):
        return None
    
    mid = (start + end) // 2
    
    node = TreeNode(list[mid])

    node.left = createMinimalTree(list, start, mid - 1)
    node.right = createMinimalTree(list, mid + 1, end)
    
    return node

tree = minimaltTree([1,2,3,4,5,6,7])


tree.display()
    
    