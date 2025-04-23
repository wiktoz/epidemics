import networkx as nx
import os
import json

from node import Node

class Graph():
    def __init__(self, path):
        try:
            if not os.path.isfile(path):
                raise FileNotFoundError(f"File '{path}' not found.")

            with open(path, "r") as f:
                data = json.load(f)

            self.G = nx.node_link_graph(data)
            self.pos = nx.spring_layout(self.G)
            bc = nx.betweenness_centrality(self.G)

            print(self.G.nodes)

            for node in self.G.nodes:
                graph_node = self.G.nodes[node]

                new_node = Node(graph_node["device_metrics"], graph_node["os_metrics"], graph_node["protection_metrics"], node, bc[node], graph_node["state"]).get_node()
                print("Node: ", new_node, "\n")

                self.G.nodes[node].update(new_node)


        except FileNotFoundError as e:
            print(f"[Error] {e}")

        except json.JSONDecodeError as e:
            print(f"[Error] Invalid JSON format: {e}")

        except Exception as e:
            print(f"[Error] Unexpected error: {e}")

    def get_graph(self):
        return self.G
    
    def get_pos(self):
        return self.pos

    