from Graph import Graph, GraphNode



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
    (nodeA, nodeD),
    (nodeF, nodeB),
    (nodeB, nodeD),
    (nodeF, nodeA),
    (nodeD, nodeC)
]

for from_node, to_node in edges:
    graph.add_edge(from_node, to_node)

graph.display_graph()