# main.py

import numpy as np
import config
from environment import Environment
from population import Population
from mutation import mutate_population
from selection import proportional_selection, threshold_selection
from reproduction import asexual_reproduction
from visualization import plot_population, plot_phys_space, plot_bars, plot_lines, plot_line
import time
import matplotlib.pyplot as plt

# main.py

import os
import numpy as np
import config
from environment import Environment
from population import Population
from mutation import mutate_individual
from selection import proportional_selection, threshold_selection
from reproduction import asexual_reproduction
from visualization import plot_population
from petri import Petri
import re

def extract_number(filename):
    match = re.search(r'frame_(\d+)\.png', filename)
    return int(match.group(1)) if match else float('inf')

def create_gif_from_frames(frames_dir, gif_filename, duration=0.1):
    """
    Łączy wszystkie obrazki z katalogu `frames_dir` w jeden plik GIF.
    Wymaga biblioteki imageio (pip install imageio).
    :param frames_dir: folder z plikami .png
    :param gif_filename: nazwa pliku wyjściowego GIF
    :param duration: czas wyświetlania jednej klatki w sekundach
    """
    import imageio
    import os

    # Sortujemy pliki po nazwach, żeby zachować kolejność generacji
    filenames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")], key=extract_number)

    with imageio.get_writer(gif_filename, mode='I', duration=duration) as writer:
        for file_name in filenames:
            path = os.path.join(frames_dir, file_name)
            image = imageio.imread(path)
            writer.append_data(image)

def main():


    '''env = Environment(alpha_init=config.alpha0, c=config.c, delta=config.delta, carbon=config.carbon)
    pop = Population(size=config.N, n_dim=config.n)



    for generation in range(config.max_generations):

        # 2. Selekcja
        survivors = threshold_selection(pop, env.get_optimal_phenotype(), config.sigma, config.threshold, env.get_current_carbon())
        pop.set_individuals(survivors)
        print(len(survivors)," przetrwało")
        if len(survivors) > 0:
            fit_chosen = proportional_selection(pop, env.get_optimal_phenotype(), config.sigma, pop.get_size(), env.get_current_carbon())
            print(len(set(fit_chosen))," gotowych do rozrodu")
            unfit_chosen = list(set(survivors)-set(fit_chosen))
            print(len(unfit_chosen)," z trudnościami")
        else:
            print(f"Wszyscy wymarli w pokoleniu {generation}. Kończę symulację.")
            break

        # 3. Reprodukcja tja(w przykładzie jest już wbudowana w selekcję)

        spawned = asexual_reproduction(fit_chosen,config.maxN)
        print(len(spawned)," nowych")

        # 1. Mutacja
        # mutate_population(pop, mu=config.mu, mu_c=config.mu_c, xi=config.xi)

        for ind in spawned:
            mutate_individual(ind,1,config.mu_c,config.xi)

        for ind in unfit_chosen:
            mutate_individual(ind,config.mu,config.mu_c,config.xi)

        pop.add_individuals(spawned)

        print(pop.get_size()," in total")

        # 4. Zmiana środowiska
        env.update(len(survivors))'''

    # Katalog, w którym zapisujemy obrazki (możesz nazwać np. "frames/")
    frames_dir = "frames"
    os.makedirs(frames_dir, exist_ok=True)  # tworzy folder, jeśli nie istnieje

    # Katalog, w którym zapisujemy obrazki (możesz nazwać np. "frames/")
    frames_dir2 = "physical frames"
    os.makedirs(frames_dir2, exist_ok=True)  # tworzy folder, jeśli nie istnieje

    frames_dir_s0 = "frames_s0"
    os.makedirs(frames_dir_s0, exist_ok=True)
    frames_dir_s1 = "frames_s1"
    os.makedirs(frames_dir_s1, exist_ok=True)
    frames_dir_s2 = "frames_s2"
    os.makedirs(frames_dir_s2, exist_ok=True)
    frames_dir_s3 = "frames_s3"
    os.makedirs(frames_dir_s3, exist_ok=True)
    frames_dir_s4 = "frames_s4"
    os.makedirs(frames_dir_s4, exist_ok=True)

    dish = Petri()

    spawn_rate_t = [[0] for s in range(int(config.plate_length/config.sector_length))]
    #spawn_start = [[0] for s in range(int(config.plate_length/config.sector_length))]
    mut_rate_t = [[0] for s in range(int(config.plate_length/config.sector_length))]
    #mut_start = [[0] for s in range(int(config.plate_length/config.sector_length))]
    death_rate_t = [[] for s in range(int(config.plate_length/config.sector_length))]
    #death_start = [[0] for s in range(int(config.plate_length/config.sector_length))]
    all_populations = [[0] for s in range(int(config.plate_length/config.sector_length))]

    all_spawn_rates = [0]
    all_mut_rates = [0]
    all_death_rates = [0]
    all_population = [0]

    avg_spawn_rate = [[0,0] for s in range(int(config.plate_length/config.sector_length))]
    avg_mut_rate = [[0,0] for s in range(int(config.plate_length/config.sector_length))]
    avg_death_rate = [[0,0] for s in range(int(config.plate_length/config.sector_length))]

    for generation in range(config.max_generations):

        # Zapis aktualnego stanu populacji do pliku PNG
        frame_filename = os.path.join(frames_dir, f"frame_{generation:03d}.png")
        plot_population(dish.get_population(), config.alpha0, generation, save_path=frame_filename, show_plot=False)

        # Zapis aktualnego stanu populacji do pliku PNG
        frame_filename = os.path.join(frames_dir2, f"frame_{generation:03d}.png")
        plot_phys_space(dish.get_population(), generation, save_path=frame_filename, show_plot=False)

        #'''
        frame_filename = os.path.join(frames_dir_s0, f"frame_{generation:03d}.png")
        plot_population(dish.get_big_sector_population(0), config.alpha0, generation, save_path=frame_filename, show_plot=False)

        frame_filename = os.path.join(frames_dir_s1, f"frame_{generation:03d}.png")
        plot_population(dish.get_big_sector_population(1), config.alpha0+config.cc, generation, save_path=frame_filename, show_plot=False)

        frame_filename = os.path.join(frames_dir_s2, f"frame_{generation:03d}.png")
        plot_population(dish.get_big_sector_population(2), config.alpha0+config.cc*2, generation, save_path=frame_filename, show_plot=False)

        frame_filename = os.path.join(frames_dir_s3, f"frame_{generation:03d}.png")
        plot_population(dish.get_big_sector_population(3), config.alpha0+config.cc*3, generation, save_path=frame_filename, show_plot=False)

        frame_filename = os.path.join(frames_dir_s4, f"frame_{generation:03d}.png")
        plot_population(dish.get_big_sector_population(4), config.alpha0+config.cc*4, generation, save_path=frame_filename, show_plot=False)
        #'''


        print("generacja", generation)


        pop, spawn, mut, death, og_pop = dish.run_all()

        #print("spawn =",spawn)
        #print("or",sum(spawn),"?")

        all_spawn_rates.append(float(sum(spawn)/sum(og_pop)))
        #print(all_spawn_rates)
        all_mut_rates.append(float(sum(mut)/sum(og_pop)))
        #print(all_mut_rates)
        all_death_rates.append(float(sum(death)/sum(og_pop)))
        #print(all_death_rates)
        all_population.append(sum(pop))

        #print(avg_death_rate)

        for s_i, s_pop in enumerate(og_pop) :

            all_populations[s_i].append(pop[s_i])

            if s_pop > 0:
                avg_spawn_rate[s_i][0] = avg_spawn_rate[s_i][0] + spawn[s_i]/og_pop[s_i]
                avg_spawn_rate[s_i][1] = avg_spawn_rate[s_i][1] + 1

                avg_mut_rate[s_i][0] = avg_mut_rate[s_i][0] + mut[s_i]/og_pop[s_i]
                avg_mut_rate[s_i][1] = avg_mut_rate[s_i][1] + 1

                avg_death_rate[s_i][0] = avg_death_rate[s_i][0] + death[s_i]/og_pop[s_i]
                avg_death_rate[s_i][1] = avg_death_rate[s_i][1] + 1

                spawn_rate_t[s_i].append(spawn[s_i]/og_pop[s_i])
                mut_rate_t[s_i].append(mut[s_i]/og_pop[s_i])
                death_rate_t[s_i].append(death[s_i]/og_pop[s_i])

            else:

                spawn_rate_t[s_i].append(0)
                mut_rate_t[s_i].append(0)
                death_rate_t[s_i].append(0)

        #print(all_spawn_rates)
        #print(avg_spawn_rate)

        #print(avg_death_rate)





    categories = ["sector 0", "sector 1", "sector 2", "sector 3", "sector 4"]

    plot_line(all_spawn_rates, "Total spawn rate in time", "Time or generations", "Spawn rate", "all_spawn_rate")
    plot_line(all_mut_rates, "Total mutation rate in time", "Time or generations", "Mutation rate", "all_mut_rate")
    plot_line(all_death_rates, "Total death rate in time", "Time or generations", "Death rate", "all_death_rate")
    plot_line(all_population, "Total population in time", "Time or generations", "Population", "all_population")


    plot_bars(avg_spawn_rate, "Average spawn rate per sector", "Sectors", "Spawn rate (new spawned/old total)", "avg_spawn_rate", categories)
    plot_bars(avg_mut_rate, "Average mutation rate per sector", "Sectors", "Mutation rate (Mutated/population)", "avg_mut_rate", categories)
    plot_bars(avg_death_rate, "Average death rate per sector", "Sectors", "Death rate (Dead/population)", "avg_death_rate", categories)

    plot_lines(spawn_rate_t, "Spawn rates in time", "Time or generations", "Spawn rate", "spawn_rates", categories)
    plot_lines(mut_rate_t, "Mutation rates in time", "Time or generations", "Mutation rate", "mut_rates", categories)
    plot_lines(death_rate_t, "Death rates in time", "Time or generations", "Death rate", "death_rates", categories)
    plot_lines(all_populations, "Population totals in time", "Time or generations", "Population", "all_populations", categories)


    print("Symulacja zakończona. Tworzenie GIF-a...")

    # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
    create_gif_from_frames(frames_dir, "simulation.gif")
    print("GIF zapisany jako simulation.gif")

    # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
    create_gif_from_frames(frames_dir2, "simulation_phys.gif")
    print("GIF zapisany jako simulation_phys.gif")

    #'''
    create_gif_from_frames(frames_dir_s0, "simulation_s0.gif")
    print("GIF zapisany jako simulation_s0.gif")

    create_gif_from_frames(frames_dir_s1, "simulation_s1.gif")
    print("GIF zapisany jako simulation_s1.gif")

    create_gif_from_frames(frames_dir_s2, "simulation_s2.gif")
    print("GIF zapisany jako simulation_s2.gif")

    create_gif_from_frames(frames_dir_s3, "simulation_s3.gif")
    print("GIF zapisany jako simulation_s3.gif")

    create_gif_from_frames(frames_dir_s4, "simulation_s4.gif")
    print("GIF zapisany jako simulation_s4.gif")
    #'''




if __name__ == "__main__":
    start_time = time.time()
    main()
    print("- %s sekund -" % (time.time() - start_time))

    '''frames_dir = "frames"

    frames_dir2 = "physical frames"


    # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
    create_gif_from_frames(frames_dir, "simulation.gif")
    print("GIF zapisany jako simulation.gif")

    # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
    create_gif_from_frames(frames_dir2, "simulation_phys.gif")
    print("GIF zapisany jako simulation_phys.gif")'''