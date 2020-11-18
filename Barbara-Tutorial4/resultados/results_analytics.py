import pandas as pd
import numpy as np
from pyfiglet import Figlet

files = ['lau15_dist-results.csv', 'kn57_dist-results.csv',
         'sgb128_dist-results.csv', 'wg22_dist-results.csv',
         'wg59_dist-results.csv']

means = []

f = Figlet(font='slant')
print(f.renderText('Ant System'))

for file in files:
    df = pd.read_csv(file, index_col=None)
    df.sort_values(by=['n_cities'], inplace=True)
    print("n_cities: {:<4} min: {:<8} mean: {:<8}  std: {:<8}".format(df['n_cities'][0], np.min(df['fo']), np.mean(df['fo']),
                                                            np.std(df['fo'])))
    # f"{df['n_cities'][0]}{' ' * 6}min: {np.min(df['fo'])} {' ' * 5} mean: {np.mean(df['fo'])} {' ' * 5} std: {np.std(df['fo'])}")
