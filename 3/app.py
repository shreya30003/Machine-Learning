# import libraries
import numpy as np

from flask import Flask, render_template,request
import pickle # Initialize the flask App

app = Flask(__name__)
model = pickle.load(open('startup.pkl', 'rb'))

# default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

# To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    # For rendering results on HTML GUI
    RD = request.form['R_D Spend']
    Admin = request.form['Administration']
    Market = request.form['Marketing Spend']
    State = request.form['State']
    
    prediction = model.predict([[float(RD), float(Admin), float(Market), float(State)]])

    output = round(prediction[0], 2) 
    return render_template('index.html', prediction_text='output : {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
