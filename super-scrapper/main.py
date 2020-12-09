from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return "Hello! Welcome to root page!"

@app.route("/contact")
def contact():
    return "Contack me!"

app.run()
