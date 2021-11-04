from flask import Flask, render_template

webapp = Flask(__name__)

@webapp.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    webapp.run()