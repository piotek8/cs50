from cs50 import SQL
from flask import Flask, render_template, request
from helpers import random_string
import random

app = Flask(__name__)

db = SQL("sqlite:///history.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            page = int(request.form.get("page"))
            if page < 0:
                return render_template("index.html", placeholder="Type in a positive number only!")
            if not isinstance(page, int):
                return render_template("index.html", placeholder="Enter a number!")

            db.execute("INSERT INTO history (page) SELECT ? WHERE NOT EXISTS (SELECT 1 FROM history WHERE page = ?)", page, page)

            random.seed(page)
            print(page)
        except ValueError:
            return render_template("index.html", placeholder="Invalid input! Please enter a valid positive integer.")

    string = random_string(1000)
    rows = db.execute("SELECT * FROM history ORDER BY page ASC;")

    return render_template("index.html",placeholder=string, name="Carter", history=rows)

