# reproduction.py

import copy

import numpy as np
import selection


def asexual_reproduction(survivors, maxN):
    """
    Wersja bezpłciowa (klonowanie):
    - Zakładamy, że potomków będzie tyle, aby utrzymać rozmiar populacji = N.
    - W najprostszej wersji: jeżeli mamy M ocalałych, 
      a M < N, to klonujemy ich losowo aż do uzyskania N osobników.
    """

    if len(survivors) == 0:
        # Zabezpieczenie: jeśli wszyscy wymarli, inicjujemy od nowa (albo zatrzymujemy symulację).
        return []

    spawn = [copy.deepcopy(ind) for ind in survivors]

    '''while len(new_population) < maxN:
        #parent = copy.deepcopy(survivors[0])  # np. zawsze klonuj pierwszego (do testów)
        # W praktyce można klonować losowo: 
        parent = copy.deepcopy(np.random.choice(survivors))
        new_population.append(parent)'''

    if len(spawn)+len(survivors)<=maxN:
        return spawn
    else:
        return spawn[:(maxN-len(survivors))]

    #return new_population[:maxN]  # przycinamy, gdyby było za dużo
