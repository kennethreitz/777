import networkx as nx
from pyvis.network import Network

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

# Define Jungian concepts
ego = "Kenneth"
shadow = "Jade"
self_node = "Self"
anima_animus = "Anima/Animus"
persona = "Persona"

# Define switchable and external alters
male = ["Keith", "Shakti", "Seven", "Ricky", "Kenneth", "Keith", "Lucky", "Metatron", "Thoth"]
female = ["Jade", "Iris", "Amber", "Iris"]

# Create the network
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


# Connect nodes based on their relationships
connect_all(network, [ego, shadow, self_node, anima_animus, persona])
connect_all(network, [ego] + male)
connect_all(network, [ego] + female)

# Additional connections (from the original code)
# ... [include other connections here as needed]

# Assign colors for the nodes based on Jungian concepts and types of alters
colors = {
    ego: "purple",
    shadow: "black",
    self_node: "gold",
    anima_animus: "cyan",
    persona: "green",
}

for alter in male:
    colors[alter] = "red"

for alter in female:
    colors[alter] = "blue"

# Pyvis visualization
nt_refactored = Network(notebook=True, width="100%", height="600px")
nt_refactored.from_nx(network)
nt_refactored.toggle_physics(True)
nt_refactored.show_buttons(filter_=["physics"])

# Apply colors
for node in nt_refactored.nodes:
    node_id = node["id"]
    if node_id in colors:
        node["color"] = colors[node_id]

# Display the network
nt_refactored.show("refactored_pyvis_network.html")
