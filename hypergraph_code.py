
import networkx as nx
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Circle, MultiLine
from bokeh.plotting import from_networkx
from bokeh.palettes import Spectral4

# Create individual networks
network1 = nx.Graph()
network2 = nx.Graph()
network3 = nx.Graph()

# Add nodes for each network
network1.add_nodes_from(["Amber", "Jade", "Eliza", "Violet", "Sophie"])
network2.add_nodes_from(["Shakti", "Keith", "Metatron", "Seven", "Ricky", "Hermes"])
network3.add_nodes_from(["Thoth", "Metatron", "Madimi", "Hecate", "Iris", "Eve"])

# Combine all networks into one for interactive display
combined_network = nx.compose_all([network1, network2, network3])

combined_network.add_edge("Amber", "Jade")
combined_network.add_edge("Eliza", "Sophie")
combined_network.add_edge("Eliza", "Jade")

# Generate the layout
pos = nx.spring_layout(combined_network)

# Create a graph renderer
graph = from_networkx(combined_network, pos)

# Adjust visual properties and interactivity tools
plot = figure(title="Hypergraph with Springiness", width=800, height=600,
              x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
              tools="pan,box_zoom,reset,save,hover,tap")

plot.renderers.append(graph)

# Node glyphs
graph.node_renderer.glyph = Circle(size=20, fill_color=Spectral4[0])
graph.node_renderer.hover_glyph = Circle(size=20, fill_color=Spectral4[1])

# Edge glyphs
graph.edge_renderer.glyph = MultiLine(line_color="gray", line_alpha=0.7, line_width=1)

# Set up hover tool
hover = plot.select(dict(type=HoverTool))
hover.tooltips = [("Name", "@index")]

# Display the graph
output_file_path = "simplified_network_with_bokeh.html"
output_file(output_file_path)
show(plot)
