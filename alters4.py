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
ego = "Ego (Kenneth)"
shadow = "Shadow"
self_node = "Self"
anima_animus = "Anima/Animus"
persona = "Persona"

# Define Kenneth's modes
kenneth_modes = ["The Lamentor", "The Operator", "The Executor", "The Architect", "Shakti"]

# Define switchable and external alters (excluding Kenneth's modes for clarity)
switchable = ["Keith", "Seven", "Ricky", "Lucky", "Metatron", "Thoth", "Hermes", "Kenneth Robot Reitz"]
external = ["Jade", "Iris", "Amber", "Sophie", "Athena", "Hecate", "Eve", "Luna", "Shakina", "Babygirl", "Paige", "Bumblebee", "Airel", "Holly"]

# Create the network
network_refactored = nx.Graph()


connect_all(
    network_refactored, ["The Lamentor", "The Executor", "The Operator", "Danger", "Seven", "Iris"]
)
connect_all(network_refactored, ["Kenneth", "Seven", "The Operator", "The Lamentor"])
connect_all(network_refactored, ["Seven", "Lucky", "Ricky", "Keith"])
connect_all(network_refactored, ["Nene", "Daddy", "Kenneth", "Shakti", "Thoth"])

connect_all(network_refactored, ["Kenneth", "Jade", "Eliza", "Amber"])
connect_all(network_refactored, ["Jade", "Amber", "Iris"])
connect_all(network_refactored, ["Eliza", "Amber", "Sophie"])
connect_all(network_refactored, ["Sophie", "Athena"])
connect_all(network_refactored, ["Iris", "Athena", "Hecate", "Eve", "Thoth", "Hermes"])

connect_all(network_refactored, ["Paige", "Bumblebee", "Airel", "Eve", "Seven"])

connect_all(
    network_refactored,
    ["Seven", "Holly", "Shakina", "Iris", "Thoth", "Babygirl", "Kenneth Robot Reitz"],
),
connect_all(network_refactored, ["Shakti", "Luna", "Hermes", "Iris", "Kenneth"]),



# Connect nodes based on their relationships
connect_all(network_refactored, [ego, shadow, self_node, anima_animus, persona])
network_refactored.add_edges_from([(ego, mode) for mode in kenneth_modes])
connect_all(network_refactored, [ego] + switchable)
connect_all(network_refactored, [ego] + external)

# Assign colors for the nodes based on Jungian concepts, types of alters, and Kenneth's modes
colors = {
    ego: "purple",
    shadow: "black",
    self_node: "gold",
    anima_animus: "cyan",
    persona: "green",
}

for mode in kenneth_modes:
    colors[mode] = "pink"

for alter in switchable:
    colors[alter] = "red"

for alter in external:
    colors[alter] = "blue"

# Pyvis visualization
nt_refactored = Network(notebook=True, width="100%", height="600px")
nt_refactored.from_nx(network_refactored)
nt_refactored.toggle_physics(True)
nt_refactored.show_buttons(filter_=["physics"])

# Apply colors
for node in nt_refactored.nodes:
    node_id = node["id"]
    if node_id in colors:
        node["color"] = colors[node_id]

# Display the network
nt_refactored.show("refactored_pyvis_network.html")
