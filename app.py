import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = nx.Graph()
pos = nx.spring_layout(G)


def animate(i):
    color = "blue"

    if i%2 == 0:
        color = "red"

    
    G["A"]["B"]["color"] = color

    plt.clf()
    plt.cla()

    edge_colors = nx.get_edge_attributes(G,'color').values()

    nx.draw(G, pos=pos, edge_color=edge_colors)

def main():

    fig = plt.figure()
    net = fig.add_subplot(111)

    nodes = [
        ("A", {"state": "S"}), "B", "C", "D"]
    edges = [
        ("A", "B", {"weight": 4, "color": "blue"}), 
        ("B", "C", {"color": "blue"}), 
        ("A", "D", {"color": "blue"}), 
        ("A", "C", {"color": "blue"})
    ]

    
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    nx.draw(G)

    pos = nx.spring_layout(G)

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()



if __name__ == "__main__":
    main()