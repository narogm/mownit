import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def generate_graph(n, sem):
    G = nx.connected_watts_strogatz_graph(n, 4, 0.5)
    i = 1
    for (e1, e2) in G.edges():
        G.edges[e1, e2].update(R=random.randint(1, 5), no=i, sem=0)
        i += 1
    if G.has_edge(0, 1):
        G.edges[0, 1].update(R=0, sem=sem)
    else:
        G.add_edge(0, 1, R=0, no=i, sem=sem)
    return G


def generate_cubical_graph(sem):
    G = nx.cubical_graph()
    i = 1
    for (e1, e2) in G.edges():
        if i == 1:
            G.edges[e1, e2].update(R=0, no=i, sem=sem)
        else:
            G.edges[e1, e2].update(R=random.randint(1, 5), no=i, sem=0)
        i += 1
    return G


def generate_graph_with_bridges(n, sem):
    G = nx.connected_watts_strogatz_graph(n, 4, 0.5)
    G2 = nx.connected_watts_strogatz_graph(n, 4, 0.5)
    G = nx.disjoint_union(G, G2)
    i = 1
    for (e1, e2) in G.edges():
        G.edges[e1, e2].update(R=random.randint(1, 5), no=i, sem=0)
        i += 1
    node = random.randint(0, n-1)
    node2 = random.randint(0, n-1)
    while node == node2:
        node2 = random.randint(0, n-1)
    G.add_edge(node, 2*n-1-node, R=0, no=i, sem=sem)
    G.add_edge(node2, 2*n-1-node2, R=random.randint(1, 5), no=i + 1, sem=0)
    return G


def generate_grid_graph(n, sem):
    G = nx.grid_2d_graph(n, n)
    i = 1
    for (e1, e2) in G.edges():
        G.edges[e1, e2].update(R=random.randint(1, 5), no=i, sem=0)
        i += 1
    node = random.randint(0, n-2)
    G.edges[(node, node), (node, node+1)].update(R=0, sem=sem)
    return G


def get_equations(G):
    equations = []
    u = []
    E = len(G.edges)
    # 1 prawo Kirchoffa
    for i in G.nodes:
        eq = [0 for i in range(E)]
        for e in G.edges(i):
            data = G.get_edge_data(*e)
            if e[0] > e[1]:
                eq[data['no']-1] = 1
            else:
                eq[data['no']-1] = -1
        equations.append(eq)
        u.append(0)
    # 2 prawo Kirchoffa
    for cycle in nx.cycle_basis(G):
        eq = [0 for i in range(E)]
        u.append(0)
        for i in range(len(cycle)):
            V1 = cycle[i]
            V2 = cycle[(i+1) % len(cycle)]
            data = G.get_edge_data(V1, V2)
            if V1 > V2:
                eq[data['no']-1] = data['R']
                u[-1] += data['sem']
            else:
                eq[data['no']-1] = -data['R']
                u[-1] -= data['sem']
        equations.append(eq)
    return equations, u


def assign_values(G):
    equations, u = get_equations(G)
    result = np.linalg.lstsq(equations, u, rcond=None)[0]   # wyliczenie wartosci I
    digraph = nx.DiGraph()
    for e in G.edges:
        I = result[G[e[0]][e[1]]['no']-1]
        if I > 0:
            digraph.add_edge(max(e[0], e[1]), min(e[0], e[1]), I=I)
        else:
            digraph.add_edge(min(e[0], e[1]), max(e[0], e[1]), I=-I)
    return digraph


def verify(G):
    for n in G.nodes:
        i_out = sum([G.edges[e]['I'] for e in G.out_edges(n)])
        i_in = sum([G.edges[e]['I'] for e in G.in_edges(n)])
        result = abs(i_in-i_out)
        if result > 10e-8:
            return False
    return True


def print_graph(G):
    pos = nx.spring_layout(G)   # dla grafu spojnego i grafu z mostami
    # pos = nx.spectral_layout(G)   # dla grafu kubicznego i siatki
    values = [round(G[e1][e2]['I'], 4) for e1, e2 in G.edges()]
    nx.draw_networkx(G, pos, edges=G.edges(),
                     node_size=15,
                     edge_color=values,
                     edge_cmap=plt.cm.jet,
                     draw_lables=False)
    labels = nx.get_edge_attributes(G, 'I')
    for label in labels:
        val = labels.get(label)
        v = round(val, 2)
        labels[label] = v
    nx.draw_networkx_edge_labels(G, pos, font_size=8, edge_labels=labels)
    plt.show()


def check_all_types(n, sem):
    G = generate_graph(n, sem)
    G = assign_values(G)
    assert verify(G)
    G = generate_graph_with_bridges(n, sem)
    G = assign_values(G)
    assert verify(G)
    G = generate_cubical_graph(sem)
    G = assign_values(G)
    assert verify(G)
    G = generate_grid_graph(n, sem)
    G = assign_values(G)
    assert verify(G)


def show_all():
    G = generate_graph(8, 10)
    G = assign_values(G)
    assert verify(G)
    print_graph(G)

    G = generate_graph_with_bridges(8, 10)
    G = assign_values(G)
    assert verify(G)
    print_graph(G)

    G = generate_cubical_graph(10)
    G = assign_values(G)
    assert verify(G)
    print_graph(G)

    G = generate_grid_graph(4, 10)
    G = assign_values(G)
    assert verify(G)
    print_graph(G)


# check_all_types(50, 10)
show_all()

# G = generate_graph(1000, 20)
# G = assign_values(G)
# assert verify(G)
