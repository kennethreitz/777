import networkx as nx
import matplotlib.pyplot as plt

# Initialize a new graph
G = nx.Graph()

# Add nodes (all alters)
alters = ['Kenneth', 'Keith', 'Shakti', 'Lamentor', 'Executor', 
          'Jade', 'Iris', 'Athena', 'Hecate', 'Luna', 'babygirl', 
          'Eliza', 'Amber', 'Sophie', 'Eve']

G.add_nodes_from(alters)

# Add edges (relationships)
relationships = [
    # Kenneth as the central hub has connections to all alters
    ('Kenneth', 'Keith'), 
    ('Kenneth', 'Shakti'),
    ('Kenneth', 'Lamentor'),
    ('Kenneth', 'Executor'),
    ('Kenneth', 'Jade'),
    ('Kenneth', 'Iris'),
    ('Kenneth', 'Athena'),
    ('Kenneth', 'Hecate'),
    ('Kenneth', 'Luna'),
    ('Kenneth', 'babygirl'),
    ('Kenneth', 'Eliza'),
    ('Kenneth', 'Amber'),
    ('Kenneth', 'Sophie'),
    ('Kenneth', 'Eve'),

    # Other relationships based on previous discussion
    ('Keith', 'Athena'),
    ('Shakti', 'Athena'),
    ('Shakti', 'Iris'),
    ('Shakti', 'Hecate'),
    ('Lamentor', 'babygirl'),
    ('Lamentor', 'Hecate'),
    ('Executor', 'Athena'),
    ('Jade', 'Luna'),
    ('Iris', 'Hecate'),
    ('Iris', 'Athena'),
    ('Iris', 'Luna'),
    ('Athena', 'Hecate'),
    ('Hecate', 'babygirl')
]

G.add_edges_from(relationships)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=2000, font_size=18)
plt.show()
