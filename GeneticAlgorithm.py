import random
import numpy as np

def genetic_algorithm(graph, population_size, num_generations, max_colors):
    population = [generate_individual(graph, max_colors) for _ in range(population_size)]
    fitness_scores = [fitness_function(graph, individual) for individual in population]

    for _ in range(num_generations):
        new_population = []

        # Keep the best individual
        best_individual = population[np.argmax(fitness_scores)]
        new_population.append(best_individual)

        # Generate the rest of the population through crossover and mutation
        for _ in range(1, population_size):
            parent1 = select_parent(graph, population, fitness_scores)
            parent2 = select_parent(graph, population, fitness_scores)

            offspring = crossover(graph, parent1, parent2, max_colors)
            offspring = mutate(graph, offspring, max_colors)

            new_population.append(offspring)

        population = new_population
        fitness_scores = [fitness_function(graph, individual) for individual in population]

    best_individual = population[np.argmax(fitness_scores)]
    return best_individual

def generate_individual(graph, max_colors):
    chromosome = {}
    for node in graph.keys():
        neighbors = graph[node]
        available_colors = set(range(max_colors)) - set(chromosome.get(neighbor, 0) for neighbor in neighbors)
        chromosome[node] = random.choice(list(available_colors))
    return chromosome



def fitness_function(graph, individual):
    score = 0
    for node in graph.keys():
        neighbors_colors = [individual[neighbor] for neighbor in graph[node]]
        if individual[node] in neighbors_colors:
            score += 1
    return score

def select_parent(graph, population, fitness_scores):
    total_fitness = sum(fitness_scores)

    if total_fitness > 0:
        return population[random.choices(range(len(population)), weights=fitness_scores, k=1)[0]]
    else:
        # If total fitness is zero, choose a parent uniformly at random
        return random.choice(population)

def crossover(graph, parent1, parent2, max_colors):
    crossover_point = random.choice(list(parent1.keys()))

    offspring = {}
    for node in graph.keys():
        if node < crossover_point:
            offspring[node] = parent1[node] % max_colors
        else:
            neighbors_colors = [offspring.get(neighbor, parent2[neighbor]) for neighbor in graph[node]]
            available_colors = [color % max_colors for color in range(max_colors) if color not in neighbors_colors]
            if available_colors:
                offspring[node] = random.choice(available_colors)
            else:
                # If no available colors, inherit the color from parent2
                offspring[node] = parent2[node] % max_colors

    return offspring

def mutate(graph, individual, max_colors):
    mutation_rate = 0.1
    for node in individual.keys():
        if random.random() < mutation_rate:
            neighbors_colors = [individual.get(neighbor, individual[node]) for neighbor in graph[node]]
            available_colors = [color % max_colors for color in range(max_colors) if color not in neighbors_colors]
            if available_colors:
                individual[node] = random.choice(available_colors)
            else:
                # If no available colors, choose a random color
                individual[node] = random.randint(0, max_colors - 1)

    return individual

def chromosome_to_graph(graph, chromosome):
    individual_graph = {}
    for node, color in chromosome.items():
        individual_graph[node] = [neighbor for neighbor in graph[node] if chromosome[neighbor] != color]
    return individual_graph



def chromatic_number(coloring):
    return len(set(coloring.values()))
