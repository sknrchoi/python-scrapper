"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from export import save_to_cvs

db = {}
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    jobs = []
    word = request.args.get("word")
    if word:
        word = word.lower()
        db_jobs = db.get(word)
        if db_jobs:
            jobs = db_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception("word argument not exist.")
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception("scrapped job in db not exist.")
        save_to_cvs(jobs)
        return send_file(
            "jobs.csv", attachment_filename=f"{word}.csv", as_attachment=True) # downloading under a different file name
    except Exception as e:
        print("Exception:", e)
        return redirect("/")


if __name__ == '__main__':
    app.run("0.0.0.0")
