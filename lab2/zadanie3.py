import numpy as np
import networkx as nx
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl


def read_file(file):
    records = []
    with open(file, "r") as data:
        buffor = csv.reader(data)
        for row in buffor:
            records.append(row)
    return records


def make_graph(records):
    G = nx.Graph()
    for i, record in enumerate(records):
        G.add_edge(record[0], record[1], R=abs(int(record[2])), no=i + 1, sem=0)
    return G


def get_equations(G):
    equations = []
    b = []
    E = len(G.edges)
    # 1 prawo Kirchoffa
    for i in G.nodes:
        eq = [0 for i in range(E)]
        for e in G.edges(i):
            data = G.get_edge_data(*e)
            if e[0] > e[1]:
                eq[data['no']] = 1
            else:
                eq[data['no']] = -1
        equations.append(eq)
        b.append(0)
    # 2 prawo Kirchoffa
    for cycle in nx.cycle_basis(G):
        eq = [0 for i in range(E)]
        b.append(0)
        for i in range(len(cycle)):
            V1 = cycle[i]
            V2 = cycle[(i+1) % len(cycle)]
            data = G.get_edge_data(V1, V2)
            if V1 > V2:
                eq[data['no']] = data['R']
                b[-1] += data['sem']
            else:
                eq[data['no']] = -data['R']
                b[-1] -= data['sem']
        equations.append(eq)
    return equations, b


records = read_file("small.csv")
G = make_graph(records)
G.add_edge('1', '4', R=0, no=0, sem=3)
equations, b = get_equations(G)
result = np.linalg.lstsq(equations, b, rcond=None)[0]

digraph = nx.DiGraph()
for e in G.edges:
    G[e[0]][e[1]]['I'] = result[G[e[0]][e[1]]["no"]]
    if G[e[0]][e[1]]['I'] > 0:
        digraph.add_edge(max(e[0], e[1]), min(e[0], e[1]), I=G[e[0]][e[1]]['I'])
    else:
        digraph.add_edge(min(e[0], e[1]), max(e[0], e[1]), I=abs(G[e[0]][e[1]]['I']))

pos = nx.layout.spring_layout(digraph)

node_sizes = [30 for i in range(len(digraph))]
M = digraph.number_of_edges()
edge_colors = range(2, M + 2)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]

nodes = nx.draw_networkx_nodes(digraph, pos, node_size=node_sizes, node_color='blue')
edges = nx.draw_networkx_edges(digraph, pos, node_size=node_sizes, arrowstyle='->',
                               arrowsize=10, edge_color=edge_colors,
                               edge_cmap=plt.cm.winter, width=2, with_labels=True)
# set alpha value for each edge
for i in range(M):
    edges[i].set_alpha(edge_alphas[i])

pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.winter)
pc.set_array(edge_colors)
plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_off()
plt.show()
