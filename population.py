# population.py

import config
import numpy as np
from individual import Individual
from scipy.stats import truncnorm

class Population:
    """
    Klasa przechowuje listę osobników (Individual)
    oraz pomaga w obsłudze różnych operacji na populacji.
    """
    def __init__(self, size, n_dim):
        """
        Inicjalizuje populację losowymi fenotypami w n-wymiarach.
        :param size: liczba osobników (N)
        :param n_dim: wymiar fenotypu (n)
        """
        self.individuals = []

        mean_x = (config.lower_x+config.upper_x)/2
        mean_y = (config.lower_y+config.upper_y)/2
        std = 0.1

        ax, bx = (config.lower_x - mean_x) / std, (config.upper_x - mean_x) / std
        ay, by = (config.lower_y - mean_y) / std, (config.upper_y - mean_y) / std

        for _ in range(size):
            # przykładowo inicjalizujemy fenotypy w okolicach [0, 0, ..., 0]
            phenotype = np.random.normal(loc=0.0, scale=1.0, size=n_dim)

            #print(phenotype)

            coordinates = [truncnorm.rvs(ay, by, loc=mean_y, scale=std), truncnorm.rvs(ax, bx, loc=mean_x, scale=std)]

            #print(coordinates)

            self.individuals.append(Individual(phenotype, coordinates))

    def get_individuals(self):
        return self.individuals

    def set_individuals(self, new_individuals):
        self.individuals = new_individuals
        #print(len(new_individuals), "survived")

    def add_individuals(self, new_individuals):
        self.individuals.extend(new_individuals)
        #print(len(new_individuals), "new")

    def add_individual(self, new_individual):
        self.individuals.append(new_individual)
        #print(1, " new")

    def get_size(self):
        return len(self.individuals)

    def set_population(self, size, n_dim, lower_y, upper_y, lower_x, upper_x ):

        mean_x = (lower_x + upper_x) / 2
        mean_y = (lower_y + upper_y) / 2
        std = 0.1

        ax, bx = (lower_x - mean_x) / std, (upper_x - mean_x) / std
        ay, by = (lower_y - mean_y) / std, (upper_y - mean_y) / std

        for _ in range(size):
            # przykładowo inicjalizujemy fenotypy w okolicach [0, 0, ..., 0]
            phenotype = np.random.normal(loc=0.0, scale=1.0, size=n_dim)

            # print(phenotype)

            coordinates = [truncnorm.rvs(ay, by, loc=mean_y, scale=std), truncnorm.rvs(ax, bx, loc=mean_x, scale=std)]

            # print(coordinates)

            self.individuals.append(Individual(phenotype, coordinates))

Population(2,2)