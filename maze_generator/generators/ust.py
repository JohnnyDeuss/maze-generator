import networkx as nx
from dppy.exotic_dpps import UST


def invert_dict(d):
    return {v: k for k, v in d.items()}


def ust(w, h):
    """
    Calculate a uniform spanning tree for our 2D grid.
    """
    g = nx.grid_2d_graph(w, h)
    # DPPy can't handle complex label names, so remap them.
    mapping = dict(enumerate(g.nodes))
    g = nx.relabel_nodes(g, invert_dict(mapping))
    # Sample a spanning tree.
    ust = UST(g)
    ust.sample("Wilson")
    st = ust.list_of_samples[0]
    # Relabel it back to the original complex names.
    nx.relabel_nodes(st, mapping, copy=False)
    return st
