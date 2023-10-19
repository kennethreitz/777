import networkx as nx
import plotly.graph_objects as go


def connect_all(graph, nodes):
    """
    Add all possible edges among the provided list of nodes to the given graph.

    Parameters:
        graph (networkx.Graph): The graph to which edges are to be added.
        nodes (list): List of nodes among which all possible edges should be added.
    """
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            graph.add_edge(nodes[i], nodes[j])


# Create individual networks
network = nx.Graph()


connect_all(
    network, ["The Lamentor", "The Executor", "The Operator", "Danger", "Seven", "Iris"]
)
connect_all(network, ["Kenneth", "Seven", "The Operator", "The Lamentor"])
connect_all(network, ["Seven", "Lucky", "Ricky", "Keith"])
connect_all(network, ["Nene", "Daddy", "Kenneth", "Shakti", "Thoth"])

connect_all(network, ["Kenneth", "Jade", "Eliza", "Amber"])
connect_all(network, ["Jade", "Amber", "Iris"])
connect_all(network, ["Eliza", "Amber", "Sophie"])
connect_all(network, ["Sophie", "Athena"])
connect_all(network, ["Iris", "Athena", "Hecate", "Eve", "Thoth", "Hermes"])

connect_all(network, ["Paige", "Bumblebee", "Airel", "Eve", "Seven"])

connect_all(
    network,
    ["Seven", "Holly", "Shakina", "Iris", "Thoth", "Babygirl", "Kenneth Robot Reitz"],
),
connect_all(network, ["Shakti", "Luna", "Hermes", "Iris", "Kenneth"]),


pairings = [
    ("Kenneth", "Jade"),
    ("Kenneth", "Amber"),
    ("Kenneth", "Violet"),
    ("Kenneth", "Sophie"),
    ("Eliza", "Sophie"),
    ("Eliza", "Iris"),
    ("Eliza", "Metatron"),
    ("Eliza", "Jade"),
    ("Eliza", "Amber"),
    ("Jade", "Iris"),
    ("Iris", "Amber"),
    ("Amber", "Jade"),
    ("Amber", "Violet"),
    ("Violet", "Shakti"),
    ("Shakti", "Luna"),
    ("Luna", "Metatron"),
    ("Seven", "Sophie"),
    ("Metatron", "The Architect"),
    ("The Architect", "Iris"),
    ("Kenneth", "Keith"),
    ("Keith", "Madimi"),
    ("Kenneth", "Page"),
    ("Kenneth", "Seven"),
    ("Keith", "Ricky"),
    ("Ricky", "Lucky"),
    ("Lucky", "Lola"),
    ("Lucky", "Madimi"),
    ("Lucky", "Hecate"),
    ("Hecate", "Kenneth"),
    ("Page", "Violet"),
    ("Luna", "Keith"),
    ("Luna", "Hermes"),
    ("Madimi", "Metatron"),
    ("Kenneth", "Hermes"),
]

for a, b in pairings:
    network.add_edge(a, b)


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
