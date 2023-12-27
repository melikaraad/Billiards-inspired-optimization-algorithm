import random
from Fitness import fitnessFunc, generate_random_vector

n_population = 10
n_iteration = 1000
length= 2


#Tolid Jamiat avaliye
def generate_population(n_population, length):
    population = []
    for _ in range(n_population):
        temp = generate_random_vector(length)
        fitness = fitnessFunc(temp)
        ch = {'vector': temp, 'fitness': fitness}
        population.append(ch)
    return population
