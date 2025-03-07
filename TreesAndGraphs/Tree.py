from collections import deque

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.leftChild = None
        self.rightChild = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, name):
        if self.root is None:
            self.root = TreeNode(name)
        else:
            self._insert_recursive(self.root, name)
    
    def _insert_recursive(self, node, name):
        if name < node.name:
            if node.leftChild is None:
                node.leftChild = TreeNode(name)
            else:
                self._insert_recursive(node.leftChild, name)
        else:
            if node.rightChild is None:
                node.rightChild = TreeNode(name)
            else:
                self._insert_recursive(node.rightChild, name)
    
    def search(self, name):
        return self._search_recursive(self.root, name)
    
    def _search_recursive(self, node, name):
        if node is None or node.name == name:
            return node
        elif name < node.name:
            return self._search_recursive(node.leftChild, name)
        else:
            return self._search_recursive(node.rightChild, name)
    
    def inorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.leftChild:
            self.inorder_traversal(node.leftChild, result)
        result.append(node.name)
        if node.rightChild:
            self.inorder_traversal(node.rightChild, result)
        return result
    
    def delete(self, name):
        self.root = self._delete_recursive(self.root, name)
    
    def _delete_recursive(self, node, name):
        if node is None:
            return node
        if name < node.name:
            node.leftChild = self._delete_recursive(node.leftChild, name)
        elif name > node.name:
            node.rightChild = self._delete_recursive(node.rightChild, name)
        else:
            if node.leftChild is None:
                return node.rightChild
            elif node.rightChild is None:
                return node.leftChild
            min_larger_node = self._find_min(node.rightChild)
            node.name = min_larger_node.name
            node.rightChild = self._delete_recursive(node.rightChild, min_larger_node.name)
        return node
    
    def _find_min(self, node):
        while node.leftChild is not None:
            node = node.leftChild
        return node

    def display(self):
        if not self.root:
            print("Tree is empty")
            return
        
        queue = deque([(self.root, 0)])
        levels = {}

        while queue:
            node, depth = queue.popleft()
            if depth not in levels:
                levels[depth] = []
            levels[depth].append(node.name)
            
            if node.leftChild:
                queue.append((node.leftChild, depth + 1))
            if node.rightChild:
                queue.append((node.rightChild, depth + 1))
        
        for depth in sorted(levels.keys()):
            print("Level", depth, ": ", "  ".join(levels[depth]))