from Tree import Tree

# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth

def listOfDepths(tree : Tree):
    if tree.root == None:
        return "Tree is empty"
    
    currList = []
    currList.append(tree.root)
    
    res = []
    
    while currList:
        res.append(currList)
        parents = currList
        currList = []
        
        for parent in parents:
            if parent.leftChild:
                currList.append(parent.leftChild)
            if parent.rightChild:
                currList.append(parent.rightChild)
        
    return res


tree = Tree()
values = ["John", "Alice", "Bob", "Eve", "Charlie", "David"]
values.sort()
for value in values:
    tree.insert(value)
    
res = listOfDepths(tree)
final = []

for list in res:
    currList = []
    for node in list:
        currList.append(node.name)
    final.append(currList)
    
tree.display()

print(final)