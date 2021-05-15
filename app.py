import os
from flask import (
    Flask, flash, render_template, 
    redirect, url_for)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", home=home)


@app.route("/about")
def about():
    return render_template("about.html", about=about)


@app.route("/contact")
def contact():
    return render_template("contact.html", contact=contact)


@app.route("/events")
def events():
    return render_template("events.html", events=events)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", gallery=gallery)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
