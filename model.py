import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression


data = pd.read_csv('diamonds.csv')
data = data.drop(columns='Unnamed: 0')

data = data.loc[(data[['x','y','z']]!=0).all(axis=1)]

data['volume'] = round((data['x'] * data['y'] * data['z']),1)
data = data.drop(columns=['x', 'y', 'z'])

data = data[['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'volume', 'price']]


# print("Cut: ",set(data["cut"]))
# print("Color: ",set(data["color"]))
# print("Clarity: ",set(data["clarity"]))

data['cut'] = data['cut'].map({'Ideal':1,'Good':2,'Very Good':3,'Fair':4,'Premium':5})
data['color'] = data['color'].map({'E':1,'D':2,'F':3,'G':4,'H':5,'I':6,'J':7})
data['clarity'] = data['clarity'].map({'VVS1':1,'IF':2,'VVS2':3,'VS1':4,'I1':5,'VS2':6,'SI1':7,'SI2':8})

X = data.iloc[:, :7]

# # Y = data.iloc[:, -1]
Y = data.iloc[:, 7:]

# X = pd.get_dummies(data=X, drop_first=True)


regressor = LinearRegression()
regressor.fit(X, Y)
pickle.dump(regressor, open('diamondmodeldata.pkl', 'wb'))
model = pickle.load(open('diamondmodeldata.pkl', 'rb'))