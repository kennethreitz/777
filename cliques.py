import networkx as nx

from network import network


# Find cliques in the network
cliques = nx.find_cliques(network)

# Print the cliques
for clique in cliques:
    if len(clique) > 2:
        print(clique)

# ['Kenneth', 'Jade', 'Amber']
# ['Kenneth', 'Violet', 'Shakti']
# ['Kenneth', 'Sophie', 'Eliza', 'Iris']
# ['Kenneth', 'Keith', 'Madimi', 'Metatron', 'The Architect']
# ['Jade', 'Iris', 'Amber']
# ['Violet', 'Shakti', 'Luna']
# ['Sophie', 'Eliza', 'Iris']
# ['Keith', 'Madimi', 'Metatron', 'The Architect']


# As you can see, the networkx.find_cliques() function found five cliques in the network:

# ['Kenneth', 'Jade', 'Amber', 'Violet']
# ['Sophie', 'Eliza', 'Iris', 'Metatron']
# ['Kenneth', 'Page', 'Seven']
# ['Keith', 'Ricky', 'Lucky']
# ['Luna', 'Madimi', 'Metatron']
