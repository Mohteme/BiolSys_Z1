# mutation.py

import numpy as np
import config

def mutate_individual(individual, mu, mu_c, xi):
    """
    Mutacja osobnika: 
      - Z prawdopodobieństwem mu osobnik ulega mutacji
      - Każda cecha p_i mutuje niezależnie z prawdopodobieństwem mu_c
      - Zmiana mutacyjna jest losowana z N(0, xi^2)
    """
    #j = 0
    #print(j)
    if np.random.rand() < mu:
        phenotype = individual.get_phenotype().copy()
        for i in range(len(phenotype)):
            if np.random.rand() < mu_c:
                #j = j + 1
                #print(j)
                phenotype[i] += np.random.normal(0.0, xi)
        individual.set_phenotype(phenotype)
        return 1
    else:
        return 0

def mutate_population(population, mu, mu_c, xi):
    """
    Mutuje całą populację (lista osobników).
    """
    for ind in population.get_individuals():
        mutate_individual(ind, mu, mu_c, xi)

def move_individual(individual, mo, mo_c, mo_xi):



    if np.random.rand() < mo:
        coordinates = individual.get_coordinates()
        for i in range(len(coordinates)):
            if np.random.rand() < mo_c:
                #j = j + 1
                #print(j)
                tmp = coordinates[i]
                coordinates[i] += np.random.normal(0.0, mo_xi)
                while coordinates[i] < 0 or coordinates[i] > (config.plate_width if i==0 else config.plate_length):
                    #print(coordinates,"index był poza")
                    coordinates[i] = tmp
                    coordinates[i] += np.random.normal(0.0, mo_xi)

        individual.set_coordinates(coordinates)
