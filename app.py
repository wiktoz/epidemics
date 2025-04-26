from graph import Graph
from epidemics import Epidemics

def main():
    G = Graph("graphs/nodes.json")

    epidemics = Epidemics(G)
    epidemics.start()

if __name__ == "__main__":
    main()
    