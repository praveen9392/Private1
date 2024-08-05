import tkinter as tk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# Load and preprocess the dataset
dataset = pd.read_csv("Datatraning.csv").dropna(axis=1)
encoder = LabelEncoder()
dataset["prognosis"] = encoder.fit_transform(dataset["prognosis"])
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

# Train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
final_nb_model = GaussianNB()
final_nb_model.fit(X, y)

# Get the symptom names from user input
user_symptoms = dataset.columns[:-1]

# Create a dictionary for symptom index and prediction classes
symptom_index = {}
for index, symptom in enumerate(user_symptoms):
    symptom_name = " ".join([i.capitalize() for i in symptom.split("_")])
    symptom_index[symptom_name] = index

# Function to predict disease based on symptoms
def predictDisease(symptoms):
    symptoms_list = symptoms.split(",")
    input_data = [0] * len(symptom_index)
    for symptom in symptoms_list:
        symptom = symptom.strip().capitalize()
        index = symptom_index.get(symptom, -1)
        if index != -1:
            input_data[index] = 1
    input_data = [input_data]
    nb_prediction = encoder.inverse_transform(final_nb_model.predict(input_data))[0]
    return nb_prediction

# Create the main window
window = tk.Tk()
window.title("Disease Prediction")
window.configure(bg="lightblue")  # Set background color of the window

# Create a Text widget to display all symptom names
symptoms_text = tk.Text(window, height=10, width=50, bg="lightyellow", fg="blue")
symptoms_text.insert(tk.END, "Symptoms:\n")
for symptom in symptom_index.keys():
    symptoms_text.insert(tk.END, f"{symptom}\n")
symptoms_text.pack()

# Create the label and entry for symptoms input
symptoms_label = tk.Label(window, text="Enter Symptoms:", fg="darkblue")
symptoms_label.pack()

symptoms_entry = tk.Entry(window)
symptoms_entry.pack()

# Create the prediction result label
result_label = tk.Label(window, text="Prediction Result:", fg="darkgreen")
result_label.pack()

# Function to handle the button click event
def predict():
    symptoms = symptoms_entry.get()
    prediction = predictDisease(symptoms)
    result_label.config(text="Prediction Result: " + prediction, fg="red")

# Create the predict button
predict_button = tk.Button(window, text="Predict", command=predict, bg="orange", fg="white")
predict_button.pack()

# Run the main window event loop
window.mainloop()