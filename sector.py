# sector.py
from numpy.f2py.auxfuncs import isintent_out

import config
from environment import Environment
from population import Population
from individual import Individual
from mutation import mutate_individual, move_individual
from selection import proportional_selection, threshold_selection
from reproduction import asexual_reproduction

class Sector:

    def __init__(self, env, pop, latitude, longitude, sigma):

        self.environment = env
        self.population = pop
        self.latitude = latitude
        self.longitude = longitude
        self.sigma = sigma


    def correct_sigma(self, new_s):

        self.sigma = new_s

    def get_coordinates(self):

        return (self.latitude, self.longitude)

    def is_outside_sector(self, point):
        y, x = point
        y_ur, x_ur = self.get_coordinates()

        # The square extends 1 unit down and 1 unit to the left
        return not (y_ur - 1 < y < y_ur and x_ur - 1 < x < x_ur)

    #def moves_to_sector(self, individual):
    #    self.population removes

    def get_population(self):

        return self.population

    def correct_alpha(self, c):

        self.environment.correct_alpha(c)


    def run_sector(self):

        n_mutations = 0

        # 2. Selekcja
        #print("sektor:", self.get_coordinates())
        #print("z początkowych:",self.population.get_size())

        og_pop = self.population.get_size()

        survivors = threshold_selection(self.population, self.environment.get_optimal_phenotype(), self.sigma, config.threshold,
                                        self.environment.get_current_carbon())

        died = og_pop-len(survivors)

        self.population.set_individuals(survivors)

        movable = []
        spawned = []

        if len(survivors) > 0:

            fit_chosen = proportional_selection(self.population, self.environment.get_optimal_phenotype(), self.sigma, self.population.get_size(),
                                                self.environment.get_current_carbon())

            #print(len(set(fit_chosen)), "gotowych do rozrodu")
            unfit_chosen = list(set(survivors) - set(fit_chosen))
            #print(len(unfit_chosen), "z trudnościami")

            # 3. Reprodukcja tja(w przykładzie jest już wbudowana w selekcję)

            spawned = asexual_reproduction(fit_chosen, config.maxN)
            #print(len(spawned), "spawned")

            # 1. Mutacja
            # mutate_population(pop, mu=config.mu, mu_c=config.mu_c, xi=config.xi)


            for ind in spawned:
                mutate_individual(ind, 1, config.mu_c, config.xi)
                move_individual(ind, 1, config.moo_c, config.moo_xi)
                if self.is_outside_sector(ind.get_coordinates()):
                    movable.append(ind)

            spawned = list(set(spawned) - set(movable))

            a = len(movable)

            #print("ze spawned nie rusza się:",len(spawned))


            for ind in unfit_chosen:
                n_mutations = n_mutations + mutate_individual(ind, config.mu, config.mu_c, config.xi)
                move_individual(ind, config.moo, config.moo_c, config.moo_xi)
                if self.is_outside_sector(ind.get_coordinates()):
                    movable.append(ind)

            #print(len(movable), "wychodzi z sektora")

            unfit_movable = list(set(unfit_chosen).intersection(set(movable)))

            #print("z tych z trudnościami rusza się:",len(unfit_movable))

            unfit_chosen = list(set(unfit_chosen) - set(movable))


            self.population.set_individuals(list(set(self.population.get_individuals()) - set(unfit_movable)))

            #print("z tych z trudnościami nie rusza się:",len(unfit_chosen))

            self.population.add_individuals(spawned)

        #print(self.population.get_size(), "nowy total?")

        # 4. Zmiana środowiska
        self.environment.update(len(survivors))

        #print("rusza się:",len(movable))

        return movable, self.population.get_size(), len(spawned), n_mutations, died, og_pop