from datetime import datetime

from flask import Flask, render_template

from . import app


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/secure/")
def secure():
    return render_template("secure.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/logout/")
def logout():
    return render_template("logout.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
