

import networkx as nx
import os
import sys
import ideagraph.graph as g

# change wd to ideagraph/
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Load graph from name passed as argument
graph = g.load(sys.argv[0])


def dump():
    """Persist loaded graph on exit"""
    g.save(graph, sys.argv[0])

    
def help():
    print("'q' to exit")
    print(list(funcs.keys()))

    
# Hold a string:function dict
#   mapping command line functions to functions in ideagraph.graph
funcs = {"help": help,
         "add-edge": graph.add_edge,
         "remove-edge": graph.remove_edge,
         "add-node": graph.add_node}


def interact():

    while True:
        # Prompt for command line input, which is saved as 'x'
        x = input("> ")
        if x == "q":
            break
        x = x.split(" ")
        try:
            if len(x) > 1:
                # Look up command in 'funcs' dict, and invoke it,
                #   passing any arguments as unpacked positional args
                funcs[x[0]](*x[1:])
            else:
                funcs[x[0]]()
        except KeyError:
            print("Not recognized...")
            help()

    # on exit
    dump()


# Script

interact()
    
