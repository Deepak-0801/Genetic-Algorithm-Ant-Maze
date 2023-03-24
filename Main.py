import numpy as np
from genetic_algorithm import run_genetic_algorithm
from maze_visualizer import visualize_maze, visualize_fitness

maze = np.array([[0,0,0,0,0,1,0,0],
                 [0,1,0,1,0,1,0,1],
                 [0,1,0,1,0,0,0,0],
                 [0,1,0,1,1,1,1,0],
                 [0,0,0,0,0,1,0,0],
                 [1,1,0,1,0,0,0,1],
                 [0,1,0,1,0,1,1,0],
                 [0,0,0,0,0,0,0,0]])

best_ant, fitness_history = run_genetic_algorithm()

# Visualize the best ant's path through the maze
print(f"Best ant fitness: {best_ant.fitness}")
visualize_maze(maze, ant=best_ant)

# Visualize the fitness history of the genetic algorithm
visualize_fitness(fitness_history)
