from flask import Flask, render_template, request, make_response
from datetime import datetime

webapp = Flask(__name__)

authors = []


@webapp.route("/")
def index():
    namen = "Hans"

    print(request.args)

    cookie_value = request.cookies.get("cookie_value")

    return render_template("index.html", namen=namen, datum_today=datetime.now(), cookie_value=cookie_value)


@webapp.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        author = request.form.get("author")
        authors.append(author)

    return render_template("about.html", authors=authors)


@webapp.route("/projects")
def projects():
    projects = ["Flask Projects", "Boogle", "Fakebook"]

    return render_template("projects.html", projects=projects)


@webapp.route("/set_cookie", methods=["GET", "POST"])
def set_cookie():
    if request.method == "POST":
        cookie_value = request.form.get("cookie")
        response = make_response(render_template("set_cookie.html", cookie_value=cookie_value))

        response.set_cookie("cookie_value", cookie_value)
    else:
        if request.args.get("action") == "delete":
            response = make_response(render_template("set_cookie.html", cookie_value=None))
            response.set_cookie("cookie_value", expires=0)
        else:
            cookie_value = request.cookies.get("cookie_value")
            response = make_response(render_template("set_cookie.html", cookie_value=cookie_value))

    return response


if __name__ == '__main__':
    webapp.run()