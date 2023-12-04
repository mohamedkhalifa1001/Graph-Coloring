# main.py
import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
from GeneticAlgorithm import genetic_algorithm,chromatic_number
from graph import create_graph, visualize_graph

if __name__ == "__main__":
    
    # Create a graph
    graph = create_graph()
 
     #Run the genetic algorithm
    best_solution = genetic_algorithm(graph, population_size=50,num_generations=10,max_colors=4)
    print("Best solution:", best_solution)
    print("Chromatic Number:", chromatic_number(best_solution))


    # Call the visualize_graph function with both graph and coloring and layout 
    visualize_graph(graph, best_solution)


