from network import network

from pyvis.network import Network

nt = Network(notebook=True, width="100%", height="1024px")
nt.from_nx(network)
nt.toggle_physics(False)
nt.show_buttons(filter_=["physics"])

nt.show("output.html")
