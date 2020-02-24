

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

# Hold a string:function dict
#   mapping command line functions to functions in ideagraph.graph
funcs = {}


def help():
    print("'q' to exit")
    print(list(funcs.keys()))

funcs["help"] = help

def interact():

    while True:
        x = input("> ")
        if x == "q":
            break
        x = x.split(" ")
        if len(x) > 1:
            funcs[x[0]](*x[1:])
        else:
            try:
                funcs[x[0]]()
            except KeyError:
                print("Not recognized...")
                help()

    # on exit
    dump()


# Script

interact()
    
