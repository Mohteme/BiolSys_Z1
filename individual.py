# individual.py

import numpy as np

class Individual:
    """
    Klasa opisująca pojedynczego osobnika.
    Przechowuje wektor fenotypu w n-wymiarowej przestrzeni.
    """
    def __init__(self, phenotype, coordinates):
        self.phenotype = phenotype
        self.coordinates = coordinates

    def get_phenotype(self):
        return self.phenotype

    def set_phenotype(self, new_phenotype):
        self.phenotype = new_phenotype

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates