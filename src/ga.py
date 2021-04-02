import numpy as np
from network import Network
from snake import Snake
from game import Game

GENERATION = 35
N_POPULATION = 100
PROB_MUTATION = 0.05

genomes = [Network() for _ in range(N_POPULATION)]

for i in range(1, GENERATION + 1):
    best_fitenss = -float('inf')
    best_score = -float('inf')
    sum_fitness = 0
    # Game Run & Calc Fitness
    for genome in genomes:
        snake = Snake(genome, ai=True)
        fitness, score = Game(snake).run()

        genome.fitness = fitness
        best_score = max(best_score, score)
        best_fitenss = max(best_fitenss, fitness)

    print(f'===== {i} Generation _ best-score: {best_score}, best-fitness: {best_fitenss}')

    # Selection : Elitist Preserving
    genomes.sort(key=lambda x: x.fitness, reverse=True)
    best_genomes = genomes[:10]

    new_generation = []
    for _ in range(N_POPULATION - 10):
        p1 = np.random.choice(best_genomes)
        p2 = np.random.choice(best_genomes)

        # CrossOver & Mutation
        child = p1.crossover(p2)
        child.mutation(PROB_MUTATION)
        
        new_generation.append(child)
    genomes = best_genomes + new_generation
    
