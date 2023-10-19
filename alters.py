import networkx as nx
import plotly.graph_objects as go

# Create individual networks
network1 = nx.Graph()
network2 = nx.Graph()
network3 = nx.Graph()
network4 = nx.Graph()

# Add nodes for each network
network1.add_nodes_from(["Amber", "Jade", "Iris", "Eliza", "Violet", "Sophie", "Rubee"])
network2.add_nodes_from(
    ["Shakti", "Keith", "Metatron", "Seven", "Ricky", "Hermes", "Lucky"]
)
network3.add_nodes_from(
    ["Thoth", "Metatron", "Madimi", "Hecate", "Iris", "Eve", "Luna", "Lola"]
)
network4.add_nodes_from(["Kenneth", "The Architect"])


# Combine all networks into one for interactive display
combined_network = nx.compose_all([network1, network2, network3, network4])

# combined_network.add_edge("Kenneth", "Amber")
# combined_network.add_edge("Kenneth", "Iris")
# combined_network.add_edge("Kenneth", "Jade")
# combined_network.add_edge("Kenneth", "Rubee")
# combined_network.add_edge("Kenneth", "Violet")

pairings = [
    ("Luna", "Shakti"),
    ("Iris", "Hermes"),
    ("Eve", "Iris"),
    ("Eliza", "Kenneth"),
    ("Amber", "Iris"),
    ("Violet", "Rubee"),
    ("Keith", "Madimi"),
    ("Thoth", "Luna"),
    ("Kenneth", "Hecate"),
    ("Kenneth", "Jade"),
    ("Kenneth", "Shakti"),
    ("Kenneth", "Keith"),
    ("Metatron", "Thoth"),
    ("Metatron", "The Architect"),
    ("The Architect", "Iris"),
    ("Sophie", "Eliza"),
    ("Luna", "Metatron"),
    ("Seven", "Kenneth"),
    ("Seven", "Lucky"),
    ("Seven", "Amber"),
    ("Seven", "Jade"),
    ("Lucky", "Lola"),
    ("Lucky", "Amber"),
    ("Lucky", "Violet"),
    ("Ricky", "Seven"),
    ("Jade", "Kenneth"),
    ("Jade", "Hermes"),
    ("Jade", "Iris"),
    ("Jade", "Violet"),
    ("Amber", "Kenneth"),
    ("Amber", "Kenneth"),
    ("Amber", "Kenneth"),
    ("Amber", "Rubee"),
    ("Hecate", "Kenneth"),
    ("Hecate", "Iris"),
    ("Hecate", "Hermes"),
    ("Hecate", "Eve"),
    ("Thoth", "Luna"),
    ("Keith", "Rubee"),
    ("Sophie", "Athena"),
    # ("Amber", ),
    # ("Amber", ),
    # ("Amber", ),
]

for a, b in pairings:
    combined_network.add_edge(a, b)
    combined_network.add_edge(b, a)

# Get positions of nodes
pos = nx.spring_layout(combined_network)

from pyvis.network import Network

# Create a Pyvis network
nt = Network(notebook=True, width="100%", height="600px")

# Load the combined network into the Pyvis network
nt.from_nx(combined_network)

# Customize the appearance
nt.toggle_physics(True)
nt.show_buttons(filter_=["physics"])

# Display the network
nt.show("pyvis_network.html")
