import pandas as pd
import numpy as np

games = pd.read_csv('games001.csv', sep=';')
rates = pd.read_csv('rates001.csv', sep=';')

win = rates.groupby('id').mark.mean()
games['mean_rate'] = games['id'].map(win) #вставка по ключу id
print(games)
res1 = games[['name', 'mean_rate']].sort_values(by='mean_rate', ascending=False).head(3)
print(res1)

games['comp_rate'] = np.nan
count = 0
for comp, df in games.groupby('company'):
    games.loc[games.company == comp, 'comp_rate'] = (df.mean_rate > 8).sum()


res2 = games[['company', 'comp_rate']].sort_values(by='comp_rate', ascending=False).head(1)
print(res2)

