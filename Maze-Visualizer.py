import matplotlib.pyplot as plt
import numpy as np

def visualize_maze(maze, ant=None, save_path=None):
    # Visualize the maze with optional ant path
    cmap = plt.cm.binary
    cmap.set_bad(color='red')
    plt.imshow(maze, cmap=cmap, interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    if ant is not None:
        x, y = ant.move(maze)
        plt.scatter(x, y, c='green', marker='o')
        plt.plot([0], [0], marker='o', markersize=10, color='blue')
        path_x = [0]
        path_y = [0]
        for direction in ant.path:
            if direction == 'U':
                path_y.append(path_y[-1]-1)
                path_x.append(path_x[-1])
            elif direction == 'D':
                path_y.append(path_y[-1]+1)
                path_x.append(path_x[-1])
            elif direction == 'L':
                path_y.append(path_y[-1])
                path_x.append(path_x[-1]-1)
            elif direction == 'R':
                path_y.append(path_y[-1])
                path_x.append(path_x[-1]+1)
        plt.plot(path_x, path_y, c='green', linewidth=2)
    if save_path is not None:
        plt.savefig(save_path)
    plt.show()

def visualize_fitness(fitness_history):
    # Visualize the fitness history of the genetic algorithm
    plt.plot(np.arange(len(fitness_history)), fitness_history)
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.show()
