from abc import abstractmethod, ABC
from graph import Graph
import networkx as nx

quarantine = {"state": "Q", "color": "yellow"}

class Quarantine():
    def __init__(self, quarantine_strategy):
        self.quarantine_strategy = quarantine_strategy
    
    def do_quarantine(self, graph: Graph):
        self.quarantine_strategy.apply_quarantine(graph)

class QuarantineStrategy(ABC):
    
    @abstractmethod
    def apply_quarantine(self, graph: Graph):
        pass

class SelectiveQuarantine(QuarantineStrategy):

    def apply_quarantine(self, graph: Graph):
        for node in graph.nodes:
            most_central_node = max(graph.nodes, key=lambda n: graph.nodes[n]["centrality"])

        if most_central_node != None:
            nx.set_node_attributes(graph, { most_central_node: {**quarantine} })
            print(f"Node {node} is quarantined.")



