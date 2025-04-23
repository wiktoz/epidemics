protection_metrics = {
    "none":0.9,
    "av": 0.5,
    "edr": 0.3
}

device_metrics = {
    "server":0.8,
    "workstation":0.6,
    "iot":0.4
}


os_metrics = {
    "linux":0.4,
    "windows":0.7
}


class Node:
    def __init__(self, device_type, os_type, protection_type, name, centraility, status):
        
        if device_type.lower() not in ["server", "workstation", "iot"]:
            raise ValueError("Device type must be Server, Workstation or IoT.")
        self.device_type = device_type.lower()

        if os_type.lower() not in ["windows", "linux"]:
            raise ValueError("OS type must be Linux or Windows.")
        self.os_type = os_type.lower()

        if protection_type.lower() not in ["none", "av", "edr"]:
            raise ValueError("Protection type must be AV, EDR or None.")
        self.protection_type = protection_type.lower()
        self.name = name
        self.status = status
        self.centrality = centraility

    def getInfectionProbability(self):
        return 0.4*self.centrality + 0.4*protection_metrics[self.protection_type] + 0.1*os_metrics[self.os_type] + 0.1*device_metrics[self.device_type]
    
    def getRecoveryTime(self):
        if self.protection_type == "edr":
            return 1
        elif self.protection_type == "av":
            return 5
        return 10

    def getNode(self):
        return (self.name, self.status, self.getInfectionProbability(), self.getRecoveryTime())

