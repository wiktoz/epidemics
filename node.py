from config import protection_metrics, os_metrics, device_metrics

class Node:
    def __init__(self, device_type, os_type, protection_type, name, centrality, state):
        if device_type.lower() not in device_metrics.keys():
            raise ValueError("Device type must be Server, Workstation or IoT.")
        
        if os_type.lower() not in os_metrics.keys():
            raise ValueError("OS type must be Linux or Windows.")
        
        if protection_type.lower() not in protection_metrics.keys():
            raise ValueError("Protection type must be AV, EDR or None.")
        
        self.device_type = device_type.lower()
        self.os_type = os_type.lower()
        self.protection_type = protection_type.lower()
        self.name = name
        self.state = state
        self.centrality = centrality

    def get_infection_probability(self):
        return 0.4*self.centrality + 0.4*protection_metrics[self.protection_type] + 0.1*os_metrics[self.os_type] + 0.1*device_metrics[self.device_type]
    
    def get_recovery_time(self):
        if self.protection_type == "edr":
            return 3
        elif self.protection_type == "av":
            return 6
        return 15

    def get_node(self):
        return {
            "state": self.state, 
            "color": "red" if self.state == "I" else "gray",
            "infection_prob": self.get_infection_probability(), 
            "recovery_time": self.get_recovery_time()
        }

