import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes (stations)
stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
G.add_nodes_from(stations)

# Define the interfering relationships
interfering_relationships = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'F', 'G'],
    'C': ['A', 'B', 'D', 'H'],
    'D': ['A', 'C', 'E', 'I'],
    'E': ['A', 'D', 'F', 'J'],
    'F': ['B', 'E', 'G', 'H'],
    'G': ['B', 'F', 'H', 'I'],
    'H': ['C', 'F', 'G', 'J'],
    'I': ['D', 'G', 'J'],
    'J': ['E', 'H', 'I']
}

# Add edges based on interfering relationships
for station, interfering_stations in interfering_relationships.items():
    for interfering_station in interfering_stations:
        G.add_edge(station, interfering_station)

# Draw the graph
pos = nx.spring_layout(G)  # Positions for all nodes

nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
plt.title('Radio Stations and Interfering Relationships')
plt.show()
