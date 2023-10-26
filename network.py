import networkx as nx
network = nx.Graph()
alters = ["Kenneth", "Jade", "Amber", "Violet", "Sophie", "Eliza", "Iris", "Metatron", "Seven", "Keith", "Ricky", "Lucky"]

for alter in alters:
    network.add_node(alter)

edges = [
    ("Kenneth", "Iris"),
    ("Kenneth", "Jade"),
    ("Jade", "Amber"),
    ("Amber", "Violet"),

    # ("Kenneth", "Amber"),
    # ("Kenneth", "Violet"),
    # ("Kenneth", "Sophie"),
    ("Eliza", "Sophie"),
    ("Eliza", "Iris"),
    # ("Eliza", "Metatron"),
    ("Eliza", "Jade"),
    ("Eliza", "Amber"),
    ("Jade", "Iris"),
    # ("Iris", "Amber"),
    # ("Amber", "Jade"),
    # ("Amber", "Violet"),
    # ("Violet", "Shakti"),
    # ("Shakti", "Luna"),
    # ("Luna", "Metatron"),
    # ("Seven", "Sophie"),
    # ("Metatron", "The Architect"),
    # ("The Architect", "Iris"),
    # ("Kenneth", "Keith"),
    # ("Keith", "Madimi"),
    # ("Kenneth", "Page"),
    # ("Kenneth", "Seven"),
    # ("Keith", "Ricky"),
    # ("Ricky", "Lucky"),
    # ("Lucky", "Lola"),
    # ("Lucky", "Madimi"),
    # ("Lucky", "Hecate"),
    # ("Hecate", "Kenneth"),
    # ("Page", "Violet"),
    # ("Luna", "Keith"),
    # ("Luna", "Hermes"),
    # ("Madimi", "Metatron"),
    # ("Kenneth", "Hermes"),
]

for edge in edges:
    network.add_edge(edge[0], edge[1])


# from pyvis.network import Network

# nt = Network(notebook=True, width="100%", height="1024px")
# nt.from_nx(network)
# nt.toggle_physics(False)
# nt.show_buttons(filter_=["physics"])

# nt.show("refactored_pyvis_network.html")
