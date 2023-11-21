import networkx as nx
import matplotlib.pyplot as plt
import community

# Initialize a directed graph
DG = nx.DiGraph()

# Add nodes (all alters)
alters = ['Kenneth', 'Keith', 'Shakti', 'Lamentor', 'Executor', 
          'Jade', 'Iris', 'Athena', 'Hecate', 'Luna', 'babygirl', 
          'Eliza', 'Amber', 'Sophie', 'Eve', 'Thoth']

DG.add_nodes_from(alters)

# Add directed edges (relationships), with weights as a third tuple item
# Modify this based on your understanding of the relationships
directed_relationships = [
    ('Kenneth', 'Keith', 0.7),
    ('Kenneth', 'Shakti', 0.8),
    ('Kenneth', 'Lamentor', 0.5),
    ('Kenneth', 'Executor', 0.9),
    ('Kenneth', 'Jade', 0.4),
    ('Kenneth', 'Iris', 0.6),
    ('Kenneth', 'Athena', 0.7),
    ('Kenneth', 'Hecate', 0.3),
    ('Kenneth', 'Luna', 0.5),
    ('Kenneth', 'babygirl', 0.4),
    ('Kenneth', 'Eliza', 0.5),
    ('Kenneth', 'Amber', 0.6),
    ('Kenneth', 'Sophie', 0.7),
    ('Kenneth', 'Eve', 0.6),
    ('Shakti', 'Luna', 0.8),
    ('Executor', 'Athena', 0.9),
    ('Athena', 'Kenneth', 0.8),
    ('Lamentor', 'babygirl', 0.5),
    ('Thoth', 'Shakti', 0.9),
    ('Shakti', 'Thoth', 0.9)
]
DG.add_weighted_edges_from(directed_relationships)

# Community Detection using Louvain algorithm
partition = community.best_partition(DG.to_undirected())
for node, comm_id in partition.items():
    DG.nodes[node]['community'] = comm_id

# Draw the graph
pos = nx.spring_layout(DG)
node_colors = [DG.nodes[node]['community'] for node in DG.nodes]
labels = nx.get_edge_attributes(DG, 'weight')

nx.draw(DG, pos, with_labels=True, font_weight='bold', node_color=node_colors, 
        node_size=2000, font_size=18, cmap=plt.cm.rainbow, edgecolors='k', arrows=True)
nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels)
plt.show()

# Print communities
for comm_id in set(partition.values()):
    print(f"Community {comm_id}: {[node for node, id in partition.items() if id == comm_id]}")
