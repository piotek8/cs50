import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        try:
            month = int(request.form.get('month'))
            day = int(request.form.get('day'))
            if month < 0 or day < 0:
                return render_template("index.html", placeholder="Type in a positive number only!")
        except ValueError:
            return render_template("index.html", placeholder="Enter valid numbers!")

        if not isinstance(name, str) or not name.isalpha():
            return render_template("index.html", placeholder="Enter a valid name!")

        data = db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?);", name, month, day)

        return redirect("/")
    
    else:
        rows = db.execute("SELECT name AS Name, month || '/' || day AS Birthday FROM birthdays;")

        return render_template("index.html",rows=rows)


