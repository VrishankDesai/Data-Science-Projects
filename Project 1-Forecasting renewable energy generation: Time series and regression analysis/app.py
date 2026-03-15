from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    start_year = int(request.form["start_year"])
    end_year = int(request.form["end_year"])

    df = pd.read_csv("renewable_energy.csv")

    # Convert year
    df["Year"] = pd.to_numeric(df["Year"])

    # Filter country (example: India)
    df = df[df["Entity"] == "India"]

    # Filter years
    filtered = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]

    # Create graph
    plt.figure(figsize=(10,4))

    plt.plot(filtered["Year"], filtered["Renewable-electricity-generating-capacity-per-capita"], marker="o")

    plt.title("Renewable Energy Generation")

    plt.xlabel("Year")
    plt.ylabel("Renewable-electricity-generating-capacity-per-capita")

    if not os.path.exists("static"):
        os.makedirs("static")

    graph_path = "static/forecast.png"

    plt.savefig(graph_path)
    plt.close()

    return render_template("index.html", graph=graph_path)

if __name__ == "__main__":
    app.run(debug=True)