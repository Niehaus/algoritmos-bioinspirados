import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv('results.csv', index_col=None)
df.sort_values(by=['n_cities'], inplace=True)

cities_sizes = []
avg_fo = []
for city_size in df['n_cities']:
    if city_size not in cities_sizes:
        cities_sizes.append(city_size)
        select_city_col = df[df['n_cities'] == city_size]['func_obj']
        avg_fo.append(int(round(np.mean(select_city_col.values))))

fig = go.Figure(data=[go.Table(header=dict(values=['Numero de Cidades', 'Menor Distancia Encontrada']),
                               cells=dict(values=[cities_sizes, avg_fo]))
                      ])
fig.show()
