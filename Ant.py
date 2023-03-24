import random

class Ant:
    def __init__(self, num_moves):
        self.num_moves = num_moves
        self.path = None
        self.fitness = None

    def evaluate_fitness(self, maze):
        # Evaluate the fitness of the ant's path through the maze
        self.fitness = 0
        x, y = self.move(maze)
        if maze[x][y] == 1:
            return
        visited = set()
        visited.add((x, y))
        for direction in self.path:
            if direction == 'U':
                x -= 1
            elif direction == 'D':
                x += 1
            elif direction == 'L':
                y -= 1
            elif direction == 'R':
                y += 1
            if x < 0 or x >= maze.shape[0] or y < 0 or y >= maze.shape[1]:
                return
            if (x, y) in visited:
                return
            visited.add((x, y))
            if maze[x][y] == 1:
                return
            self.fitness += 1

    def move(self, maze):
        # Follow the ant's path through the maze to determine its current location
        x = 0
        y = 0
        for direction in self.path:
            if direction == 'U':
                x -= 1
            elif direction == 'D':
                x += 1
            elif direction == 'L':
                y -= 1
            elif direction == 'R':
                y += 1
            if x < 0 or x >= maze.shape[0] or y < 0 or y >= maze.shape[1]:
                return -1, -1
            if maze[x][y] == 1:
                return -1, -1
        return x, y

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness


def generate_random_ant(num_moves):
    # Generate a random ant with a specified number of moves
    ant = Ant(num_moves)
    ant.path = ''.join(random.choice(['U', 'D', 'L', 'R']) for _ in range(num_moves))
    return ant


def crossover(parent1, parent2):
    # Perform crossover between two ants
    crossover_point = random.randint(0, parent1.num_moves-1)
    child = Ant(parent1.num_moves)
    child.path = parent1.path[:crossover_point] + parent2.path[crossover_point:]
    return child


def mutate(ant):
    # Mutate an ant by randomly changing one move in its path
    mutation_index = random.randint(0, ant.num_moves-1)
    mutation_direction = random.choice(['U', 'D', 'L', 'R'])
    ant.path = ant.path[:mutation_index] + mutation_direction + ant.path[mutation_index+1:]
