import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp



# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///avalanche.db")

@app.route("/", methods=["GET", "POST"])
def home():
        return render_template("home.html")

@app.route("/data", methods=["GET", "POST"])
def lookup():
    
    if request.method == "POST":
        # lookup the avalanche score in databade
        locations = request.form.get("location")
        
        stats = db.execute("SELECT location, grade, direction FROM avalanche WHERE location = ?", locations)
        
        #scrape website if says e.g limite then convert that to a grade 2

        # if not stock_quote:
        #     return apology("Stock does not exist", 400)

        # if not request.form.get("symbol"):
        #     return apology("must provide symbol", 400)
        
        return render_template("data.html", locations = locations, stats=stats)

    else:
        # display home page again
        return render_template("home.html")





