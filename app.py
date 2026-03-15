from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    fever = int(request.form['fever'])
    cough = int(request.form['cough'])
    headache = int(request.form['headache'])
    vomiting = int(request.form['vomiting'])

    prediction = model.predict([[fever,cough,headache,vomiting]])

    return "<h2>Predicted Disease: " + prediction[0] + "</h2>"

if __name__ == "__main__":
    app.run(debug=True)