from queue import Empty, PriorityQueue

import networkx as nx
import numpy as np


def best_first(w, h):
    """
    Generate a maze using a best first search. The output is a 2D lattice graph
    that represents the maze.
    """
    g = nx.grid_2d_graph(w, h)
    priorities = np.arange(w * h)
    np.random.shuffle(priorities)
    priorities = dict(zip(g.nodes, priorities))
    nx.set_node_attributes(g, priorities, "priority")
    nx.set_node_attributes(g, None, "queued_by")
    nx.set_edge_attributes(g, False, "is_path")

    queue = PriorityQueue()

    start = next(n for n, priority in g.nodes(data="priority") if priority == 0)
    queue.put((0, start))

    try:
        while item := queue.get(block=False):
            _, n_to = item
            # Mark the edge leading into this square as a path in the maze.
            if n_from := g.nodes[n_to]["queued_by"]:
                g.get_edge_data(n_from, n_to)["is_path"] = True
            # Queue all neighbors that aren't queued already.
            neighbors = [
                n for n in g.neighbors(n_to) if g.nodes[n]["queued_by"] is None
            ]
            for n in neighbors:
                g.nodes[n]["queued_by"] = n_to
                queue.put((g.nodes[n]["priority"], n))
    except Empty:
        # Remove all edges that represent walls.
        wall_edges = [e for e in g.edges(data="is_path") if not e[2]]
        g.remove_edges_from(wall_edges)
        return g
    raise Exception("Unreachable code")
