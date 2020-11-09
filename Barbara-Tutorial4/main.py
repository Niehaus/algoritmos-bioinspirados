def le_arquivo(filepath):
    global data

    data = {'dist_matrix': {}, 'pheromone_matrix': {}}

    with open(filepath, 'r') as dist_matrix_file:
        for i, line in enumerate(dist_matrix_file, start=1):
            data['dist_matrix'][i] = line.split()
            data['pheromone_matrix'][i] = [0] * len(line.split())


if __name__ == '__main__':
    global data
    le_arquivo('lau15_dist.txt')
