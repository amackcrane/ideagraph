
from networkx import MultiDiGraph


class Node:

    def __init__(self, id, text):
        self.id = id
        self.text = text


class IdeaGraph(MultiDiGraph):
    """Extension of networkx.MultiDiGraph to parse custom Node class nicely"""

    def add_edge(self, id1, id2, type=None):
        """Parse string ID arguments into Nodes
        Unlike networkx's Graph classes, node must already exist
        in graph (via e.g. g.add_node())"""
        pass

    def add_undirected_edge(self, id1, id2, type=None):
        pass

    def remove_edge(self, id1, id2):
        pass

    def remove_undirected_edge(self, id1, id2):
        pass

    def add_node(text):
        """Create a node with the given text
        Allocating an ID automatically"""
        pass
    

def load(graphname):
    """Return graph object read from file"""
    pass

def save(graph, name):
    """Pickle graph object under data/<name>"""
    pass


