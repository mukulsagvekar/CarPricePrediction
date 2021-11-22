import re
from flask import Flask, render_template, redirect, request
import pickle
from flask.helpers import url_for
import pandas as pd
import numpy as np
from datetime import date
#import cloudpickle as cp
#from urllib.request import urlopen

app = Flask(__name__)

model = pickle.load(open('rf_model.pkl', 'rb'))
#model=cp.load(urlopen('https://drive.google.com/file/d/1hR-3s1RbedpW8dLtOQio_ULeEz62QtdZ/view?usp=sharing','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    today = date.today()
    petrol=0
    diesel=0
    cng=0
    lpg=0
    manual=0
    auto=0
    dealer=0
    trusted_dealer=0
    individual=0
    first=0
    second=0
    third=0
    forth=0
    test=0
    if request.method == 'POST':
        year = int(request.form['year'])
        km = int(request.form['km'])
        mileage = float(request.form['mileage'])
        cc = int(request.form['cc'])
        power = float(request.form['power'])
        seat = int(request.form['seat'])

        n_year = today.year - year
        print(n_year)
        fuel_type = request.form['fuel']
        if fuel_type=='Diesel':
            diesel=1
        elif fuel_type=='Petrol':
            petrol=1
        elif fuel_type=='CNG':
            cng=1
        elif fuel_type=='LPG':
            lpg=1
        
        transmission_type = request.form['transmission']
        if transmission_type == 'Manual':
            manual=1
        elif transmission_type == 'Automatic':
            auto=1

        seller_type = request.form['seller']
        if seller_type=='Dealer':
            dealer=1
        elif seller_type=='Trusted Dealer':
            trusted_dealer=1
        elif seller_type=='Individual':
            individual=1

        owner = request.form['owners']
        if owner=='First Owner':
            first=1
        elif owner=='Second Owner':
            second=1
        elif owner=='Third Owner':
            third=1
        elif owner=='Forth Owner':
            forth=1
        elif owner=='Test Drive Car':
            test=1

        X=[[km, seat, mileage, cc, power, diesel, lpg, petrol, individual, trusted_dealer, manual, forth, second, test, third, n_year]]
        #print(X)
        output = model.predict(X)
        #print(round(output[0],2))
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:

            return render_template('index.html',prediction_text="You Can Sell The Car at Rs.    {}".format(round(output[0],2)))     
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
