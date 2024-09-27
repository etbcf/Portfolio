from flask import Flask
from flask import abort
from flask import render_template

app = Flask(__name__)

projects = [
    {
        "name": "Hábitos em Python e MongoDB",
        "thumb": "images/habit-tracking.png",
        "hero": "images/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-ztfe.onrender.com"
    }
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route('/')
def home():
    return render_template("home.html", projects=projects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/project/<string:slug>')
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
