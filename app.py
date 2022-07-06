from flask import Flask, render_template
import pandas as pd
import csv
import joblib


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

@app.route("/pred", method = ['POST'])
def prediction():
    comp = request.form['company']
    year2 = request.form['year']
    kms = request.form['kms_driven']
    model1 = request.form['car_models']
    fuel = request.form['fuel_type']
    loaded_model = joblib.load("model/LinearRegressionModel.pkl")
    loaded_model.predict()



if __name__ == "__main__":
    app.run(debug=True)
