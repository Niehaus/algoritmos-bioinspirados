from ant_system import AntSystem, Ant
import sys
import csv
import os


def read_file(filepath):
    global data

    data = {'dist_matrix': {}, 'pheromone_matrix': {}, 'city_number': 0}

    with open(filepath, 'r') as dist_matrix_file:
        for i, line in enumerate(dist_matrix_file, start=0):
            data['dist_matrix'][i] = list(map(int, line.split()))
            data['pheromone_matrix'][i] = [10 ** -16] * len(line.split())
        data['city_number'] = len(data['dist_matrix'])


def write_results(file):
    if os.path.isfile(file):
        with open(file, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(
                {'n_cities': data['city_number'], 'fo': optimum, 'iterations': iter_max,
                 'evaporation': evaporation_rate})
    else:
        with open(file, 'w+', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(
                {'n_cities': data['city_number'], 'fo': optimum, 'iterations': iter_max,
                 'evaporation': evaporation_rate})


if __name__ == '__main__':
    global data

    read_file(sys.argv[3])

    alpha = 1
    beta = 5
    Q = 100
    evaporation_rate = float(sys.argv[2])
    iter_max = int(sys.argv[1])
    iteration = 0
    ant_system = AntSystem(data, alpha, beta, Q, evaporation_rate)

    ant_pop = Ant.generate_ant_pop(data['city_number'])
    while iteration < iter_max:
        for ant in ant_pop:
            ant.prepare_for_tour()
            ant_system.move(ant)
            ant_system.update_best_solution(ant.trail)
        ant_system.update_pheromone(ant_pop)
        iteration += 1
    ant_system.clear_pheromone_matrix()
    optimum, solution = ant_system.get_best_solution()
    print(f"Número de Cidades: {data['city_number']} \nSolução: {optimum} : {solution}")

fieldnames = ['n_cities', 'fo', 'iterations', 'evaporation']
file = f"{sys.argv[3].replace('.txt', '')}-results.csv"
write_results(file)
