import pandas as pd


data = pd.read_csv('data/diamonds.csv')
data = data.drop(columns='Unnamed: 0')

data['volume'] = round((data['x'] * data['y'] * data['z']),1)
data = data.drop(columns=['x', 'y', 'z'])
data = data.to_pickle('data/diamondsdata.pkl')
# d1= pd.read_pickle('data/diamondsdata.pkl')
# print(d1.head())
