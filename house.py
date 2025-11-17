import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor # fits multiple decision tree on random samples of data and averages the rsult to improve data and reduce overfitting
from sklearn.metrics import mean_squared_error, r2_score
import joblib #libraay to import the large objects
housing = fetch_california_housing()
data = pd.DataFrame(housing.data, columns = housing.feature_names)
data['PRICE'] = housing.target
data.head(5)
X = data.drop('PRICE', axis = 1)
Y = data['PRICE']
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
scaler = StandardScaler() #mean 0 and SD 1
X_trained_scaler = scaler.fit_transform(X_train) 
X_test_scaler = scaler.transform(X_test) # uses test stats from training data to maintain consistency
model = RandomForestRegressor(n_estimators=100, random_state= 42)#builds 100 Decision Trees
model.fit(X_trained_scaler,y_train)
y_pred =model.predict(X_test_scaler)
mse = mean_squared_error(y_test, y_pred)
r2 =r2_score(y_test,y_pred) #how well the model has done the prediction compare to actual values
print('MSE is',mse)
print('R squared is',r2)
joblib.dump(model, 'calfornia_model.pkl')
#to load model
model = joblib.load('calfornia_model.pkl')
predictions = model.predict(X_test_scaler) #predictions from loaded model
print('predictions from loaded model',predictions[:5]) # same as y_pred