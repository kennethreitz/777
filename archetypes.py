import networkx as nx
import matplotlib.pyplot as plt

# Define the archetypes
archetypes = [
    "The Self",
    "The Shadow",
    "The Anima/Animus",
    "The Persona",
    "The Father",
    "The Mother",
    "The Child",
    "The Wise Old Man/Woman",
    "The Hero",
    "The Trickster",
    "The Maiden",
    "The Lover",
    "The Destroyer",
    "The Creator",
    "The Sage",
    "The Explorer",
    "The Ruler",
    "The Magician"
]

# Define the relationships between archetypes
related_archetypes = [
    ("The Self", "The Shadow"),
    ("The Self", "The Anima/Animus"),
    ("The Self", "The Persona"),
    ("The Self", "The Wise Old Man/Woman"),
    ("The Self", "The Hero"),
    ("The Self", "The Creator"),
    ("The Self", "The Sage"),
    ("The Self", "The Explorer"),
    ("The Self", "The Magician"),
    ("The Shadow", "The Anima/Animus"),
    ("The Shadow", "The Persona"),
    ("The Shadow", "The Wise Old Man/Woman"),
    ("The Shadow", "The Hero"),
    ("The Shadow", "The Trickster"),
    ("The Shadow", "The Destroyer"),
    ("The Shadow", "The Sage"),
    ("The Shadow", "The Explorer"),
    ("The Shadow", "The Ruler"),
    ("The Shadow", "The Magician"),
    ("The Anima/Animus", "The Persona"),
    ("The Anima/Animus", "The Wise Old Man/Woman"),
    ("The Anima/Animus", "The Hero"),
    ("The Anima/Animus", "The Sage"),
    ("The Anima/Animus", "The Explorer"),
    ("The Persona", "The Wise Old Man/Woman"),
    ("The Persona", "The Hero"),
    ("The Persona", "The Sage"),
    ("The Persona", "The Explorer"),
    ("The Father", "The Child"),
    ("The Father", "The Wise Old Man/Woman"),
    ("The Father", "The Hero"),
    ("The Father", "The Ruler"),
    ("The Father", "The Magician"),
    ("The Mother", "The Child"),
    ("The Mother", "The Wise Old Man/Woman"),
    ("The Mother", "The Hero"),
    ("The Mother", "The Ruler"),
    ("The Mother", "The Magician"),
    ("The Child", "The Wise Old Man/Woman"),
    ("The Child", "The Hero"),
    ("The Child", "The Innocent"),
    ("The Child", "The Orphan"),
    ("The Child", "The Jester"),
    ("The Child", "The Caregiver"),
    ("The Child", "The Seeker"),
    ("The Wise Old Man/Woman", "The Hero"),
    ("The Wise Old Man/Woman", "The Sage"),
    ("The Wise Old Man/Woman", "The Explorer"),
    ("The Hero", "The Trickster"),
    ("The Hero", "The Maiden"),
    ("The Hero", "The Lover"),
    ("The Hero", "The Destroyer"),
    ("The Hero", "The Creator"),
    ("The Hero", "The Sage"),
    ("The Hero", "The Explorer"),
    ("The Hero", "The Ruler"),
    ("The Hero", "The Magician"),
    ("The Trickster", "The Maiden"),
    ("The Trickster", "The Lover"),
    ("The Trickster", "The Destroyer"),
    ("The Trickster", "The Creator"),
    ("The Trickster", "The Sage"),
    ("The Trickster", "The Explorer"),
    ("The Trickster", "The Ruler"),
    ("The Trickster", "The Magician"),
    ("The Maiden", "The Lover"),
    ("The Maiden", "The Destroyer"),
    ("The Maiden", "The Creator"),
    ("The Maiden", "The Sage"),
    ("The Maiden", "The Explorer"),
    ("The Maiden", "The Ruler"),
    ("The Maiden", "The Magician"),
    ("The Lover", "The Destroyer"),
    ("The Lover", "The Creator"),
    ("The Lover", "The Sage"),
    ("The Lover", "The Explorer"),
    ("The Lover", "The Ruler"),
    ("The Lover", "The Magician"),
    ("The Destroyer", "The Creator"),
    ("The Destroyer", "The Sage"),
    ("The Destroyer", "The Explorer"),
    ("The Destroyer", "The Ruler"),
    ("The Destroyer", "The Magician"),
    ("The Creator", "The Sage"),
    ("The Creator", "The Explorer"),
    ("The Creator", "The Ruler"),
    ("The Creator", "The Magician"),
    ("The Sage", "The Explorer"),
    ("The Sage", "The Ruler"),
    ("The Sage", "The Magician"),
    ("The Explorer", "The Ruler"),
    ("The Explorer", "The Magician"),
    ("The Ruler", "The Magician")
]

# Create a graph and add the archetypes and relationships as nodes and edges
network = nx.Graph()
network.add_nodes_from(archetypes)
network.add_edges_from(related_archetypes)


from pyvis.network import Network

# Create a Pyvis network
nt = Network(notebook=True, width="100%", height="600px")

# Load the combined network into the Pyvis network
nt.from_nx(network)

# Customize the appearance
nt.toggle_physics(True)
nt.show_buttons(filter_=["physics"])

# Specify edge colors based on a criterion (for demonstration: edges connected to "Kenneth")
edge_colors = []
for source, target in network.edges():
    if "Kenneth" in [source, target]:
        edge_colors.append("red")  # Color for edges connected to "Kenneth"
    else:
        edge_colors.append("blue")  # Color for all other edges

# Add the edges with specified colors to the Pyvis network
for index, (source, target) in enumerate(network.edges()):
    nt.add_edge(source, target, color=edge_colors[index])

# Display the network
nt.show("pyvis_network.html")
