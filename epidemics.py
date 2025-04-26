import random
import matplotlib.pyplot as plt # type: ignore
import matplotlib.animation as animation # type: ignore
import random
import networkx as nx
from quarantine import SelectiveQuarantine, Quarantine

susceptible = {"state": "S", "color": "gray"}
infected = {"state": "I", "color": "red"}
recovered = {"state": "R", "color": "green"}

class Epidemics():
    def __init__(self, G):
        self.G = G
        self.ani = None

    def will_infect(self, prob):
        return random.random() < prob

    def advance(self, i):
        print("Step: ", i, "\n")
        graph = self.G.get_graph()
        if (i == 3):
            strategy = SelectiveQuarantine()
            quarantine = Quarantine(strategy)
            quarantine.do_quarantine(graph)
        for node in graph.nodes:
            if graph.nodes[node]["state"] == "I":
                graph.nodes[node]["recovery_time"] -= 1
                if graph.nodes[node]["recovery_time"] <= 0:
                    graph.nodes[node]["state"] = "R"
                    nx.set_node_attributes(graph, { node: {**recovered} })
                    nx.set_edge_attributes(graph, { (node, node): recovered })
                    print("Node ", node, " recovered. \n")

        for node in graph.nodes:
            if graph.nodes[node]["state"] == "I":
                for n in graph.neighbors(node):
                    print(graph.nodes[n], "\n")
                    if self.will_infect(graph.nodes[n]["infection_prob"]) and graph.nodes[n]["state"] == "S":
                        nx.set_node_attributes(graph, { n: {**infected} })
                        nx.set_edge_attributes(graph, { (n, node): infected})

        if all(graph.nodes[n]["state"] == "I" for n in graph.nodes):
            print("All nodes infected. Stopping animation.")
            self.ani.event_source.stop()

        plt.clf()
        plt.cla()

        edge_colors = nx.get_edge_attributes(graph, 'color').values()
        node_colors = nx.get_node_attributes(graph, 'color').values()

        nx.draw(graph, pos=self.G.get_pos(), with_labels=True, edge_color=edge_colors, node_color=node_colors)

    def start(self):
        fig = plt.figure()
        self.ani = animation.FuncAnimation(fig, self.advance, interval=300)
        plt.show()