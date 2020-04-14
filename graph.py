
from networkx import MultiDiGraph


class Node:

    def __init__(self, id, text):
        self.id = id
        self.text = text


class IdeaGraph(MultiDiGraph):
    """Extension of networkx.MultiDiGraph to parse custom Node class nicely"""

    def add_edge(self, id1, id2, *args):
        """Parse string ID arguments into Nodes, and create edge
        Node must already exist in graph (via g.add_node())

        Usage: add-edge id1 id2 [-t|--type <type>] [-u|--undirected]"""

        # Parse arguments
        type = None
        directed = True
        
        arg_stream = iter(args)
        for arg in arg_stream:
            # Specify node type
            if arg in ("-t", "--type"):
                try:
                    type = next(arg_stream)
                except StopIteration:
                    raise TypeError("Error: missing promised type argument in add_edge")
            # Specify undirected
            else if arg in ("-u", "--undirected"):
                directed = False
            else:
                raise TypeError("Unsupported arguments to IdeaGraph.add_edge")
        
        pass

    def remove_edge(self, id1, id2, *args):
        """Parse string IDs into nodes & remove edge"""
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

