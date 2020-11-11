from ant_system import AntSystem, Ant


def read_file(filepath):
    global data

    data = {'dist_matrix': {}, 'pheromone_matrix': {}, 'city_number': 0}

    with open(filepath, 'r') as dist_matrix_file:
        for i, line in enumerate(dist_matrix_file, start=0):
            data['dist_matrix'][i] = list(map(int, line.split()))
            data['pheromone_matrix'][i] = [10 ** -16] * len(line.split())
        data['city_number'] = len(data['dist_matrix'])


if __name__ == '__main__':
    global data

    read_file('lau15_dist.txt')

    alpha = 1
    beta = 5
    Q = 100
    evaporation_rate = 0.5
    iter_max = 3
    iteration = 0
    ant_system = AntSystem(data, alpha, beta, Q, evaporation_rate)

    ant_pop = Ant.generate_ant_pop(data['city_number'])
    while iteration < iter_max:
        # print('*' * 24, iteration, '*' * 27)
        for ant in ant_pop:
            ant.prepare_for_tour()
            ant_system.move(ant)
            ant_system.update_best_solution(ant.trail)
        ant_system.update_pheromone(ant_pop)
        iteration += 1
    ant_system.clear_pheromone_matrix()
    optimum, solution = ant_system.get_best_solution()
    print(f"Número de Cidades: {data['city_number']} \nSolução Ótima: {optimum}")
