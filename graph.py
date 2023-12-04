import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

def create_graph():
    # Get user input for the number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    # Initialize an empty graph
    graph = {str(i): [] for i in range(1, num_vertices + 1)}

    # Get user input for edges
    print("Enter edges (e.g., '1 2' represents an edge between vertex 1 and vertex 2):")
    for _ in range(num_edges):
        edge = input().split()
        if len(edge) == 2:
            vertex1, vertex2 = edge
            # Add edges for both vertices
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)

    return graph




def visualize_graph(graph, coloring):
    G = nx.Graph(graph)
    # Convert the keys of coloring to strings
    coloring = {str(vertex): color for vertex, color in coloring.items()}
    node_colors = [coloring[vertex] for vertex in G.nodes]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, font_color='black', font_weight='bold')
    plt.show()
