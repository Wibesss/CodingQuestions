class GraphNode:
    def __init__(self, name):
        self.name = name
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2):
        node1.children.append(node2)

    def display_graph(self):
        for node in self.nodes:
            connections = ", ".join(child.name for child in node.children)
            print(f"{node.name} -> {connections}")