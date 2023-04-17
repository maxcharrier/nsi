import matplotlib.pyplot as plt
import networkx as nx

graphe = nx.Graph()

graphe.add_edge("R1", "R2", weight=0.1)
graphe.add_edge("R1", "R3", weight=1)
graphe.add_edge("R2", "R3", weight=0.1)
graphe.add_edge("R2", "R4", weight=1)
graphe.add_edge("R3", "R5", weight=0.1)
graphe.add_edge("R4", "R5", weight=0.1)
graphe.add_edge("R4", "R6", weight=0.1)
graphe.add_edge("R5", "R6", weight=1)
graphe.add_edge("R5", "R7", weight=100)
graphe.add_edge("R6", "R7", weight=1)

chemin = nx.shortest_path(graphe, "R1", "R7", weight="weight")
print(f"Chemin le plus court : {chemin}")

options = {
	"node_color": "red",
	"node_size": 600,
	"edge_color": "tab:grey",
	"with_labels": True
}

nx.draw(graphe, **options)

plt.show()
