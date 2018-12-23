import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
import math
import scipy.stats as stats

T = nx.DiGraph()   # or DiGraph, etc
T.add_edges_from( ((1,2), (2,3), (2,4), (2,5), (5,2)) )
nx.draw(T, with_labels=True)
plt.show()

def rank(array):
    temp = array[:,0].argsort(axis = 0)
    ranks = temp[:,0].argsort(axis = 0)
    return ranks


def katzTina(graph, max_num_of_steps, tolerance, alpha, beta):
    start = timer()
    A = nx.adjacency_matrix(graph)
    r = A[:,0]                    #first guess for vector r is first column of A 
    diff = 1000 
    k = 0
    vector = np.ones((A.shape[1],1))
    while diff > tolerance and k < max_num_of_steps:
        r, q = alpha*A.dot(r) + beta * vector, r               #inner product of matrix Q and vector r
        diff = np.linalg.norm(q-r, ord=1)
        k += 1
    print('process finished after {} iterations'.format(k))
    end = timer()
    print('time consumption: {} seconds'.format(end-start))  #timing of the process
    return r

test = katzTina(T,100,0.1,0.2,1)


