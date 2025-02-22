from Graph import Graph, GraphNode
from collections import deque

# Given a directed graph, design an algorithm to find out 
# whether there is a route between two nodes

def findRoute(node1: GraphNode, node2: GraphNode):
    if node1 is None or node2 is None:
        return False

    if node1 == node2:  # Direct match
        return True

    visited = set()
    
    q = deque([node1])

    while q:
        curr = q.popleft()
        
        if curr in visited:
            continue
        
        visited.add(curr)

        for neighbor in curr.children:
            if neighbor == node2:  # Found the target node
                return True
            q.append(neighbor)
    
    return False

graph = Graph()

nodeA = GraphNode("A")
nodeB = GraphNode("B")
nodeC = GraphNode("C")
nodeD = GraphNode("D")
nodeE = GraphNode("E")
nodeF = GraphNode("F")

for node in [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF]:
    graph.add_node(node)

edges = [
    (nodeA, nodeB),
    (nodeA, nodeC),
    (nodeB, nodeD),
    (nodeC, nodeD),
    (nodeC, nodeE),
    (nodeE, nodeF)
]

for from_node, to_node in edges:
    graph.add_edge(from_node, to_node)

graph.display_graph()

print(findRoute(nodeA, nodeF))