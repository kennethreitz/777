import networkx as nx

from network import network


centralities = nx.centrality.degree_centrality(network)

# Print the most central alters
for alter, centrality in centralities.items():
    if centrality > 0.2:
        print(alter)


# Calculate degree centrality
degree_centrality = nx.degree_centrality(network)

# Calculate closeness centrality
closeness_centrality = nx.closeness_centrality(network)

# Calculate betweenness centrality
betweenness_centrality = nx.betweenness_centrality(network)

# Use the Louvain algorithm to detect communities
communities = nx.community.louvain_communities(network)

# Use the Girvan-Newman algorithm to detect communities
communities = nx.community.girvan_newman(network)

# Use the Fast Unfolding algorithm to detect communities
# communities = nx.community.fast_unfolding(network)


# import networkx as nx
# import matplotlib.pyplot as plt

# # Generate a community graph
# nx.draw_networkx_communities(network, communities, node_size=50, alpha=0.7)

# # Plot the community graph
# plt.axis("off")
# plt.title("Community Graph")
# plt.show()
