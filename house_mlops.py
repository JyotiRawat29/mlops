
#%%
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
housing = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target, test_size=0.2, random_state=42) # same split is done at each run
scaler = StandardScaler() #each feature contribute equally                            
X_train_scaled = scaler.fit_transform(X_train) # compute mean and SD
X_test_scaled = scaler.transform(X_test) # use stats from train
#%%
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled,y_train)
joblib.dump(model,'model_ops.pkl')

#include mlflow and logging too