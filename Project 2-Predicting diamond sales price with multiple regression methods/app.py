from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    carat = float(request.form["carat"])
    depth = float(request.form["depth"])
    table = float(request.form["table"])
    x = float(request.form["x"])
    y = float(request.form["y"])
    z = float(request.form["z"])

    features = np.array([[carat, depth, table, x, y, z]])

    prediction = model.predict(features)

    return render_template("index.html",
                           prediction_text=f"Predicted Diamond Price: ${prediction[0]:.2f}")

if __name__ == "__main__":
    app.run(debug=True)