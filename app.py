from flask import Flask, render_template, request, url_for
import pandas as pd
import csv
import joblib
import pickle
import numpy as np


app = Flask(__name__)
# car = pd.read_csv("model/cleaned data.csv")
file = open('model/cleaned data.csv')
text = csv.reader(file);
company = set()
model = set()
year1 = set()
driven = set()
# price = set()
for row in text:
      company.add(row[2])
      model.add(row[1])
      year1.add(row[3])
      driven.add(row[5])
      # price.add(row[4])
@app.route("/")
def index():
    companies = sorted(company)
    car_models = sorted(model)
    year = sorted(year1, reverse = True)
    kms_driven = sorted(driven)
    return render_template('index.html', companies = companies, car_models=car_models, year = year, kms_driven = kms_driven)

@app.route("/pred", methods = ['GET', 'POST'])
def pred():
    if request.method == "POST":
        comp = request.form['company']
        year2 = request.form['year']
        kms = request.form['kms_driven']
        model1 = request.form['car_models']
        fuel = request.form['fuel_type']
        with open("model/LinearRegressionModel.pkl", "rb") as f:
            model = pickle.load(f)
        a = [[model1, comp, year2, kms, fuel]]
        value = model.predict(pd.DataFrame(data=a, index=np.arange(len(a)),
                                           columns=["name", "company", "year", "kms_driven", "fuel_type"]))[0]
        print(value)
        return render_template('prediction.html', value=value)
    elif request.method == 'GET':
        return render_template('prediction.html', value='No values provided')
if __name__ == "__main__":
    app.run(debug=True)
