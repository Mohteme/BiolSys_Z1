# config.py

import numpy as np

# -------------------
# PARAMETRY POPULACJI
# -------------------
N = 100           # początkowa liczba osobników w populacji
maxN = 200       # maksymalna liczba osobników w populacji
n = 2             # wymiar przestrzeni fenotypowej

# --------------------
# PARAMETRY MUTACJI
# --------------------
mu = 0.5         # prawdopodobieństwo mutacji dla osobnika
mu_c = 0.1       # prawdopodobieństwo mutacji konkretnej cechy, jeśli osobnik mutuje
xi = 0.1         # odchylenie standardowe w rozkładzie normalnym

# PARAMETRY MOOVEMENTU
moo = 0.5
moo_c = 0.1
moo_xi = 0.1

lower_y = 3 #6
upper_y = 4 #7
lower_x = 0
upper_x = 1
x_lower = 27
x_upper = 26

# --------------------
# PARAMETRY SELEKCJI
# --------------------
sigma = 0.1      # parametr w funkcji fitness (kontroluje siłę selekcji)
threshold = 0.1  # przykładowy próg do selekcji progowej (do ewentualnego użycia)

# --------------------
# PARAMETRY ŚRODOWISKA
carbon = 400

# --------------------
# Początkowe alpha(t)
alpha0 = np.array([0.0, 0.0])  
# Wektor kierunkowej zmiany c
c = np.array([0.0, 0.0])
cc = np.array([0.5,0.5])
delta = 0    # odchylenie standardowe dla fluktuacji
max_generations = 3000  # liczba pokoleń do zasymulowania

# ----------------------
# PARAMETRY REPRODUKCJI
# ----------------------
# W wersji bezpłciowej zakładamy klonowanie z uwzględnieniem mutacji.
# Jeśli chcemy modelować płciowo, trzeba dodać odpowiednie parametry.

plate_length = 15 #27
plate_width = 7 #13
sector_length = 3
sigmaa = [1, 0.5, 0.3, 0.2, 0.1]
#sigmaa = [0.05, 0.1, 0.2, 0.5, 1]
#sigmaa = (1, 0.3, 0.1, 0.03, 0.01)