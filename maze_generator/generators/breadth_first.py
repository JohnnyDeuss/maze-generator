from random import randint

import networkx as nx


def breadth_first(w, h):
    """
    Generate a maze using random breadth first search. The output is a 2D
    lattice graph that represents the maze.
    """
    g = nx.grid_2d_graph(w, h)
    nx.set_node_attributes(g, None, "queued_by")
    nx.set_edge_attributes(g, False, "is_path")

    queue = []
    queue.append((randint(0, w - 1), randint(0, h - 1)))

    while queue:
        n_to = queue.pop(randint(0, len(queue) - 1))
        # Mark the edge leading into this square as a path in the maze.
        if n_from := g.nodes[n_to]["queued_by"]:
            g.get_edge_data(n_from, n_to)["is_path"] = True
        # Queue all neighbors that aren't queued already, unless this is
        # terminal square.
        if n_to != (w - 1, h - 1):
            neighbors = [
                n for n in g.neighbors(n_to) if g.nodes[n]["queued_by"] is None
            ]
            for n in neighbors:
                g.nodes[n]["queued_by"] = n_to
                queue.append(n)
    # Remove all edges that represent walls.
    wall_edges = [e for e in g.edges(data="is_path") if not e[2]]
    g.remove_edges_from(wall_edges)
    return g
