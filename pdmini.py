from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)



# Load the dataset
dataset = pd.read_csv("Data.csv")

# Split the dataset into features (X) and target (y)
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

# Encode the target value using LabelEncoder
encoder = LabelEncoder()
y_train_encoded = encoder.fit_transform(y_train)

# Train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train_encoded)

# Create a symptom index dictionary to encode the input symptoms into numerical form
symptoms = X.columns.values
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

# Define the function to predict diseases based on symptoms
def predictDisease(symptoms):
    symptoms = symptoms.split(",")
    input_data = [0] * len(symptom_index)
    for symptom in symptoms:
        index = symptom_index.get(symptom)
        if index is not None:
            input_data[index] = 1
    input_data = np.array(input_data).reshape(1, -1)
    nb_prediction = nb_model.predict(input_data)
    predicted_disease = encoder.inverse_transform(nb_prediction)
    return predicted_disease[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        predicted_disease = predictDisease(symptoms)
        return render_template('index.html', predicted_disease=predicted_disease)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
