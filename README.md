Genetic Algorithm Ant Maze
==========================

This project uses a genetic algorithm to solve a maze using an ant that can move in four directions (up, down, left, and right). The project includes several files:

-   `ant.py`: contains the code for the ant's movement and behavior.
-   `genetic-algorithm.py`: contains the code to implement the genetic algorithm, including fitness evaluation, selection, crossover, and mutation.
-   `maze-visualizer.py`: contains the code to visualize the maze and the path chosen by the ant.
-   `main.py`: runs the genetic algorithm and maze visualization.

Usage
-----

To run the program, simply run the `main.py` file. The program will generate a maze and use a genetic algorithm to find the optimal path for the ant to reach the end of the maze. The program will output a graph showing the progress in fitness for each generation, as well as a visualization of the maze and the path chosen by the ant.

Dependencies
------------

This project requires the following Python packages:

-   `numpy`
-   `matplotlib`

Implementation Details
----------------------

The genetic algorithm used in this project works as follows:

1.  Initialization: A population of random individuals (ant paths) is created.
2.  Evaluation: Each individual is evaluated by calculating its fitness (i.e., how close it gets to the end of the maze).
3.  Selection: The fittest individuals are selected to be parents for the next generation.
4.  Crossover: The selected parents are combined to create new individuals (ant paths).
5.  Mutation: The new individuals undergo random mutations to introduce new genetic material.
6.  Repeat: Steps 2-5 are repeated for a set number of generations or until the optimal path is found.

The `ant.py` file contains the code for the ant's movement and behavior. The ant can move in four directions (up, down, left, and right) and will continue to move in the same direction until it hits a wall or reaches the end of the maze. The ant's movement is determined by a list of instructions that are encoded in the ant's genetic material.

The `maze-visualizer.py` file contains the code to visualize the maze and the path chosen by the ant. The maze is generated randomly using a binary tree algorithm, and the path chosen by the ant is shown in red.

The `genetic-algorithm.py` file contains the code to implement the genetic algorithm. The fitness of each individual is calculated by measuring the distance between the ant and the end of the maze. The selection process uses a tournament selection method, and crossover and mutation are implemented using standard genetic algorithm techniques.

Future Improvements
-------------------

There are several potential improvements that could be made to this project, including:

-   Different maze generation algorithms: The project currently uses a binary tree algorithm to generate the maze, but other algorithms could be implemented to generate more complex and interesting mazes.
-   Better fitness evaluation: The current fitness function simply measures the distance between the ant and the end of the maze, but other metrics could be used to evaluate the fitness of the ant's path (e.g., number of turns, number of steps taken, etc.).
-   Tuning genetic algorithm parameters: The genetic algorithm used in this project uses default parameters, but tuning these parameters could potentially improve the performance of the algorithm and lead to faster convergence.
-   Parallelization: The genetic algorithm is currently implemented sequentially, but parallelization could be used to speed up the computation and improve performance.

Conclusion
----------

The Genetic Algorithm Ant Maze project is an interesting application of genetic algorithms to solve maze problems. The project demonstrates the use of genetic algorithms for pathfinding and maze solving problems, and provides a starting point for further exploration and experimentation with genetic algorithms. With further improvements, this project could be extended to solve more complex and challenging maze problems, and could potentially be used in real-world applications such as robotics and automation.

Credits
-------

This project was developed by [Deepak](https://github.com/Deepak-0801) as part of [SCC.361] in Lancaster University, under the guidance of [Hossein-Rahmani]. The project was developed using Python and various open-source libraries.
