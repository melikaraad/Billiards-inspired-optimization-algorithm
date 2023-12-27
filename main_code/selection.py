#ravesh entekhab dar in algorithm niz roulette_wheel_selection mibashad.

from initpopulation import  n_population, length
import random
from math import exp

beta = 0.3

def roulette_wheel_selection(population):
  
    population_fitness = sum(exp(-beta/ch['fitness']) for ch in population)
    probabilities = [exp(-beta/ch['fitness'])/population_fitness for ch in population]
    
    pockets = random.choices(population, weights= probabilities, k=5)
    return pockets
