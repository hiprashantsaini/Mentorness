from flask import Flask,request,render_template
import numpy as np
import pandas
import sklearn
import pickle
from pandas import DataFrame
# importing our model 
model=pickle.load(open('salary.pkl','rb'))
#creating flask app
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("salary.html")

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    sex = request.form['SEX']
    des = request.form['DESIGNATION']
    age = float(request.form['AGE'])
    unit = request.form['UNIT']
    rating=float(request.form['RATINGS'])
    exp =float(request.form['PAST EXP'])
    years=float(request.form['WORKING YEARS'])

    # Create a DataFrame from the input
    input_data = {'SEX': [sex], 'DESIGNATION': [des], 'AGE': [age], 'UNIT': [unit],'RATINGS':[rating],'PAST EXP': [exp],'WORKING YEARS':[years]}
    input_df = DataFrame(input_data)
    # Make the prediction
    prediction = model.predict(input_df)
    prediction=int(prediction[0])

    return render_template('salary.html', result=prediction)


#python main
if __name__ == "__main__":
    app.run(debug=True)