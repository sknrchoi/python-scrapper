from flask import Flask, render_template

app = Flask("Super-Scrapper")

@app.route("/")
def home():
    return render_template("home.html")

app.run()
