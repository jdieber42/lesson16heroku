from flask import Flask, render_template
from datetime import datetime

webapp = Flask(__name__)

@webapp.route("/")
def index():
    namen = "Hans"
    return render_template("index.html", namen=namen, datum_today=datetime.now())

@webapp.route("/about")
def about():
    authors = ["Hans", "Heike", "Monika"]

    return render_template("about.html", authors=authors)

@webapp.route("/projects")
def projects():
    projects = ["Flask Projects", "Boogle", "Fakebook"]

    return render_template("projects.html", projects=projects)

if __name__ == '__main__':
    webapp.run()