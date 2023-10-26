import networkx as nx
import matplotlib.pyplot as plt

# Create a networkx graph object
network = nx.Graph()

# Add your alters to the graph as nodes
alters = ["Kenneth", "Jade", "Amber", "Violet", "Sophie", "Eliza", "Iris", "Metatron", "Seven", "Keith", "Ricky", "Lucky"]

for alter in alters:
    network.add_node(alter)

# Add edges to the graph to represent the relationships between your alters
edges = [
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

for edge in edges:
    network.add_edge(edge[0], edge[1])

# Generate a community graph
communities = nx.community.girvan_newman(network)
print(communities)
# # Plot the community graph
# plt.figure(figsize=(10, 10))
# colors = ["red", "green", "blue", "yellow", "magenta"]
# for i, community in enumerate(communities):
#     nodes = frozenset(community)
#     nx.draw_networkx_nodes(network, nx.spring_layout(network), nodelist=nodes, node_size=50, alpha=0.7, node_color=colors[i % len(colors)])
#     nx.draw_networkx_edges(network, nx.spring_layout(network), edgelist=list(zip(nodes[:-1], nodes[1:])), alpha=0.7)
# nx.draw_networkx_labels(network, nx.spring_layout(network))
# plt.axis("off")
# plt.title("DID System Community Graph")
# plt.show()
