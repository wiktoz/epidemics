from abc import abstractmethod, ABC
from graph import Graph


class Quarantine():
    def __init__(self, quarantine_strategy):
        self.quarantine_strategy = quarantine_strategy
    
    def do_quarantine(self, graph: Graph):
        self.quarantine_strategy.apply_quarantine(graph)

class QuarantineStrategy(ABC):
    def __init__(self, quarantine_strategy):
        self.quarantine_strategy = quarantine_strategy
    
    @abstractmethod
    def apply_quarantine(self, graph: Graph):
        pass

class SelectiveQuarantine(QuarantineStrategy):

    def apply_quarantine(self, graph: Graph):
        for node in graph.get_graph().nodes:
            most_central_node = max(graph.get_graph().nodes, key=lambda n: graph.get_graph().nodes[n]["centrality"])

        if most_central_node != None:
            most_central_node["state"] = "Q"
            most_central_node["color"] = "yellow"
            print(f"Node {node} is quarantined.")



