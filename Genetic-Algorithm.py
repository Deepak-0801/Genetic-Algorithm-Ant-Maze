import random
from ant import Ant

POPULATION_SIZE = 50
MUTATION_RATE = 0.1
NUM_GENERATIONS = 100

def generate_initial_population(size):
    # Generate a list of ants with random paths
    population = []
    for i in range(size):
        path_length = random.randint(10, 50)
        path = ''.join(random.choices(['U', 'D', 'L', 'R'], k=path_length))
        ant = Ant(path)
        ant.evaluate_fitness()
        population.append(ant)
    return population

def select_parents(population):
    # Select two parents from the population using tournament selection
    parent1 = max(random.sample(population, k=5), key=lambda ant: ant.fitness)
    parent2 = max(random.sample(population, k=5), key=lambda ant: ant.fitness)
    return parent1, parent2

def crossover(parent1, parent2):
    # Perform crossover between two parents to create a child
    split_point = random.randint(1, len(parent1.path)-1)
    child_path = parent1.path[:split_point] + parent2.path[split_point:]
    child = Ant(child_path)
    return child

def mutate(ant):
    # Perform mutation on an ant's path
    new_path = ''
    for direction in ant.path:
        if random.random() < MUTATION_RATE:
            new_path += random.choice(['U', 'D', 'L', 'R'])
        else:
            new_path += direction
    mutated_ant = Ant(new_path)
    return mutated_ant

def get_fitness_sum(population):
    # Calculate the sum of the fitness values of all ants in the population
    fitness_sum = sum
    return fitness_sum

def run_generation(population):
    # Run a single generation of the genetic algorithm
    new_population = []
    for i in range(len(population)):
        parent1, parent2 = select_parents(population)
        child = crossover(parent1, parent2)
        if random.random() < MUTATION_RATE:
            child = mutate(child)
        child.evaluate_fitness()
        new_population.append(child)
    return new_population

def run_genetic_algorithm():
    # Run the genetic algorithm for a specified number of generations
    population = generate_initial_population(POPULATION_SIZE)
    best_ant = max(population, key=lambda ant: ant.fitness)
    fitness_history = [best_ant.fitness]
    for i in range(NUM_GENERATIONS):
        population = run_generation(population)
        best_ant = max(population, key=lambda ant: ant.fitness)
        fitness_history.append(best_ant.fitness)
    return best_ant, fitness_history
