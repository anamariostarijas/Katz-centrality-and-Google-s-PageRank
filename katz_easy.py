#import libraries
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
import math

T = nx.DiGraph()   # or DiGraph, etc
T.add_edges_from( ((1,2), (2,3), (2,4), (2,5), (5,2)) )
nx.draw(T, with_labels=True)
plt.show()
# R = nx.adjacency_matrix(T)

#G = nx.path_graph(4)
phi = (1 + math.sqrt(5)) / 2.0  # largest eigenvalue of adj matrix
centrality = nx.katz_centrality(G, 1/phi-0.01)
for n, c in sorted(centrality.items()):
    print("%d %0.2f" % (n, c))

