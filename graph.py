import argparse
import pandas as pd

from graph.model import Graph
from graph.shortest_path import dijkstra

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--file",
    action="store",
    dest="graph_input",
    help="Superior triangle of graph adjacency matrix",
)
parser.add_argument(
    "-d",
    "--dijkstra",
    action="store_const",
    dest="graph_method",
    const="dijkstra",
    help="Dijkstra algorithm selected",
)
parser.add_argument(
    "-p",
    "--prim",
    action="store_const",
    dest="graph_method",
    const="prim",
    help="PRIM algorithm selected",
)
parser.add_argument(
    "-k",
    "--kruskal",
    action="store_const",
    dest="graph_method",
    const="kruskal",
    help="KRUSKAL method selected",
)
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

results = parser.parse_args()

if results.graph_method == "dijkstra":
    g = Graph(results.graph_input)
    dijkstra(g, g.get_vertex(0), g.get_vertex(g.num_vertices-1))
elif results.graph_method == "prim":
    pass
elif results.graph_method == "kruskal":
    pass
