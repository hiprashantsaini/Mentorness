from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Importing our model
model = pickle.load(open('Credit_card_approval.pkl', 'rb'))

# Creating Flask app
app = Flask(__name__)

print("Ok hello")

@app.route('/')
def index():
    return render_template("credit.html")

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    gender = request.form['gender']
    has_car = request.form['hasCar']
    has_property = request.form['hasProperty']
    children_count = int(request.form['childrenCount'])
    income = float(request.form['income'])
    employment_status = request.form['employmentStatus']
    education_level = request.form['educationLevel']
    marital_status = request.form['maritalStatus']
    dwelling = request.form['dwelling']
    age = int(request.form['age'])
    employment_length = float(request.form['employmentLength'])
    has_mobile_phone = request.form['hasMobilePhone']
    has_work_phone = request.form['hasWorkPhone']
    has_phone = request.form['hasPhone']
    has_email = request.form['hasEmail']
    job_title = request.form['jobTitle']
    family_member_count = int(request.form['familyMemberCount'])
    account_age = float(request.form['accountAge'])


    income=income/100000
    # Create a DataFrame from the input
    input_data = {
        'Gender': [gender], 
        'Has a car': [has_car], 
        'Has a property': [has_property], 
        'Children count': [children_count], 
        'Income': [income], 
        'Employment status': [employment_status], 
        'Education level': [education_level], 
        'Marital status': [marital_status], 
        'Dwelling': [dwelling], 
        'Age': [age], 
        'Employment length': [employment_length], 
        'Has a mobile phone': [has_mobile_phone], 
        'Has a work phone': [has_work_phone], 
        'Has a phone': [has_phone], 
        'Has an email': [has_email], 
        'Job title': [job_title], 
        'Family member count': [family_member_count], 
        'Account age': [account_age]
    }
    input_df = pd.DataFrame(input_data)
    
    # Make the prediction
    prediction = model.predict(input_df)
    prediction = int(prediction[0])

    print("Ok hello prediction",prediction)
    if prediction== 0:
        result='No Risk'
    else:
        result='Risk'


    return render_template('credit.html', result=result)

# Python main
if __name__ == "__main__":
    app.run(debug=True)
