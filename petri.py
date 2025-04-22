# petri.py

import config
from sector import Sector
from environment import Environment
from population import Population
import individual
import math

class Petri:

    def __init__(self):

        self.sectors = [[Sector(Environment(alpha_init=config.alpha0, c=config.c, delta=config.delta, carbon=config.carbon), Population(0,config.n),i+1,j+1,0) for j in range(config.plate_length)] for i in range(config.plate_width)]


        for i in range(config.plate_width):
            for j in range(config.plate_length):
                if j >= 0:
                    s = config.sigmaa[0]
                    c = 0
                    if j >= 3:
                        s = config.sigmaa[1]
                        c = config.cc
                        if j >=6:
                            s = config.sigmaa[2]
                            c = config.cc*2
                            if j >= 9:
                                s = config.sigmaa[3]
                                c = config.cc*3
                                if j >= 12:
                                    s = config.sigmaa[4]
                                    c = config.cc*4
                self.sectors[i][j].correct_sigma(s)
                self.sectors[i][j].correct_alpha(c)
                #print("Sector ",i," ",j)

        '''
        for i in range(config.plate_width):
            for j in range(config.plate_length):
                if abs(j - 13.5) <= 13.5:
                    s = config.sigmaa[0]
                    if abs(j - 13.5) <= 10.5:
                        s = config.sigmaa[1]
                        if abs(j - 13.5) <= 7.5:
                            s = config.sigmaa[2]
                            if abs(j - 13.5) <= 4.5:
                                s = config.sigmaa[3]
                                if abs(j - 13.5) <= 1.5:
                                    s = config.sigmaa[4]
                self.sectors[i][j].correct_sigma(s)
                #print("Sector ",i," ",j)
        '''
        self.sectors[config.lower_y][0].get_population().set_population(config.N,2,config.lower_y,config.upper_y,0,1)


        #self.sectors[6][26].get_population().set_population(config.N,2,6,7,26,27)




    def run_all(self):

        move = []

        big_sector_pop = [0 for i in range(0, int(config.plate_length/config.sector_length))]

        big_sector_spawn = [0 for i in range(0, int(config.plate_length/config.sector_length))]

        big_sector_mutations = [0 for i in range(0, int(config.plate_length/config.sector_length))]

        big_sector_deaths = [0 for i in range(0, int(config.plate_length/config.sector_length))]

        big_sector_og_pop = [0 for i in range(0, int(config.plate_length/config.sector_length))]


        for _ in self.sectors:
            for j, sec in enumerate(_):

                tmp = sec.run_sector()

                move.extend(tmp[0])

                big_sector_pop[math.floor(j/3)] = big_sector_pop[math.floor(j/3)] + tmp[1]

                big_sector_spawn[math.floor(j/3)] = big_sector_spawn[math.floor(j/3)] + tmp[2]

                big_sector_mutations[math.floor(j/3)] = big_sector_mutations[math.floor(j/3)] + tmp[3]

                big_sector_deaths[math.floor(j/3)] = big_sector_deaths[math.floor(j/3)] + tmp[4]

                big_sector_og_pop[math.floor(j/3)] = big_sector_og_pop[math.floor(j/3)] + tmp[5]



        for ind in move:
            where = ind.get_coordinates()
            self.sectors[math.floor(where[0])][math.floor(where[1])].get_population().add_individual(ind)

        return big_sector_pop, big_sector_spawn, big_sector_mutations, big_sector_deaths, big_sector_og_pop

            #movement to musi być po pętli


    def get_population(self):

        pop = []

        for _ in self.sectors:
            for sec in _:
                pop.extend(sec.get_population().get_individuals())

        return pop

    def get_big_sector_population(self, i) :

        pop = Population(0, config.n)

        for _ in self.sectors:
            for j, sec in enumerate(_):
                if math.floor(j/3) == i:
                    pop.add_individuals(sec.get_population().get_individuals())

        return pop.get_individuals()


'''
dish = Petri()

#for generation in range(config.max_generations):
for generation in range(3):
    print("generacja",generation)
    dish.run_all()'''