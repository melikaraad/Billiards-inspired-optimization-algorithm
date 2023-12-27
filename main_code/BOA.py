#the answer and error I got:
#max fitness:
#{'vector': [0.6215755854709402, -0.3612345162053068], 'fitness': 1.2010668077457094}
#error:
#26.03410692656334 %

import random
from roulette_wheel_selection import roulette_wheel_selection
from initpopulation import length, generate_population, n_population
from Fitness import fitnessFunc

n_iteration = 10000
iteration = 0
main_answer = [0.5,-0.5]
population = generate_population(n_population, length)

sorted_population = sorted(population, key=lambda x: x['fitness'], reverse=True)
half_index = len(sorted_population) // 2
#first half are the ordinary balls
first_half = sorted_population[:half_index]

Pockets = roulette_wheel_selection(population)

updated_first_half = first_half.copy()

while iteration <= n_iteration :

    PR = iteration / n_iteration
    for idx, ch in enumerate(updated_first_half):
        a = [
            random.uniform(-0.1, 0.1) * (1 - PR) * (ch_elem - Pockets[idx]['vector'][i]) + Pockets[idx]['vector'][i]
            for i, ch_elem in enumerate(ch['vector'])
        ]
        b = fitnessFunc(a)
        updated_first_half[idx] = {'vector': a, 'fitness': b}

    iteration += 1


print(updated_first_half)

print('max fitness:')

max_fitness = max(updated_first_half, key=lambda x: x['fitness'])

print(max_fitness)

print('error:')

error = sum(abs((y - x) / x) * 100 for x, y in zip(main_answer, max_fitness['vector'])) / len(main_answer)


print(error)
