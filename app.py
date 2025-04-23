import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

susceptible = {"state": "S", "color": "gray"}
infected = {"state": "I", "color": "red"}

def willBeInfected(prob):
    return random.random() < prob

def animate(i, G, pos):

    for node in G.nodes:
        if G.nodes[node]["state"] == "I":
            neighbors = G.neighbors(node)
            for n in neighbors:
                if willBeInfected(G.nodes[n]["infection_prob"]):
                    G.nodes[n]["state"] = "I"

    nx.set_edge_attributes(G, { ("A", "B"): susceptible if i%2 == 0 else infected})

    plt.clf()
    plt.cla()

    edge_colors = nx.get_edge_attributes(G, 'color').values()
    node_colors = nx.get_node_attributes(G, 'color').values()

    nx.draw(G, pos=pos, edge_color=edge_colors, node_color=node_colors)

def main():
    G = nx.Graph()
    fig = plt.figure()

    nodes = [
        ("A", {**infected, "infection_prob": 0.4}), 
        ("B", {**susceptible, "infection_prob": 0.1}), 
        ("C", {**susceptible, "infection_prob": 0.2}), 
        ("D", {**susceptible, "infection_prob": 0.6}),
    ]

    edges = [
        ("A", "B", {"weight": 4, "color": "gray"}), 
        ("B", "C", {"color": "gray"}), 
        ("A", "D", {"color": "gray"}), 
        ("A", "C", {"color": "gray"})
    ]

    
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)

    ani = animation.FuncAnimation(fig, animate, interval=200, fargs=(G, pos))
    plt.show()



if __name__ == "__main__":
    main()