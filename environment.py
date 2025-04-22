# environment.py

import numpy as np
import config

class Environment:
    """
    Klasa środowiska przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, alpha_init, c, delta, carbon):
        """
        :param alpha_init: początkowy wektor alpha
        :param c: wektor kierunkowy zmiany
        :param delta: odchylenie std w losowej fluktuacji
        """
        self.alpha = alpha_init
        self.c = c
        self.delta = delta
        self.carbon = carbon

    def update(self, pop_size):
        """
        Zmiana środowiska w każdym pokoleniu:
        alpha(t) = alpha(t-1) + N(c, delta^2 I)
        """
        #n = len(self.alpha)
        #random_shift = np.random.normal(loc=self.c, scale=self.delta, size=n)
        #self.alpha = self.alpha + random_shift
        #
        self.carbon = config.carbon-pop_size
        #
        #print(self.alpha)

    def get_optimal_phenotype(self):
        return self.alpha

    def get_current_carbon(self):
        return self.carbon

    def correct_alpha(self, c):

        self.alpha = self.alpha + c