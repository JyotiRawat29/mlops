from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load('model_ops.pkl')
app = Flask(__name__) #initialises flask web app
#app will be used to define routes and handles

@app.route('/predict', methods = ['POST']) #defines URL path that user will use to interact eih API, methods says that the endpoint will accept only POST request
def predict(): #function will handle the (POST) request sent to predict
    data = request.get_json() #inputting data from user
    features = np.array(data['features']).reshape(1,-1) #preprocessing the data
    prediction = model.predict(features)[0]
    return jsonify({'prediction':prediction})

if __name__ == '__main__': #to run flask app, ensures flask app run when script is executed directly
    app.run(host='0.0.0.0', port = 5000) #at port 5000, from any network I/F in local machine
    


