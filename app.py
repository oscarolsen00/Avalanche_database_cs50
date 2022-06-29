from cs50 import SQL
from flask import Flask, redirect, render_template, request
from bs4 import BeautifulSoup
import requests


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///avalanche.db")

@app.route("/", methods=["GET", "POST"])
def home():
        return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    #get which locations are available in the database so can display them in the search drop-down menu
    locations_dict = db.execute("SELECT DISTINCT location FROM avalanche")
    locations = []
    for location_dict in locations_dict:
        locations.append(location_dict["location"])
    return render_template("search.html", locations=locations)

@app.route("/data")
def table():
    """Show all the data in one place"""
    history = db.execute("SELECT location, grade, type, time FROM avalanche")
    return render_template("table.html", history=history)

@app.route("/data", methods=["GET", "POST"])
def lookup():
    
    if request.method == "POST":
        # retrieve the locartion that is selected
        location = request.form.get("location")

        if not location:
            return redirect("/search")

        #seaarch the database for website of that given location
        url_dict = db.execute("SELECT website FROM avalanche WHERE location = ?", location)
        url = url_dict[0]["website"]
        req=requests.get(url)
        content=req.text
        #pass it through beautiful soup and get the relevant content that we want
        soup=BeautifulSoup(content,'html.parser')
        risk_block =soup.find("div", {"class" : "col-xs-6 col-sm-4 col-md-8"})
        risk_block_text = risk_block.text
        type =soup.find("div", {"class" : "description"}).h2.text
        #update database with this new content as well as the time stamp for when this was last done
        db.execute("UPDATE avalanche SET grade = ?, time = CURRENT_TIMESTAMP, type = ? WHERE location = ?", risk_block_text, type, location)


        # this is where we use fatmap to display the chosen location in an interactive way
        if location == "Lyngen":
            src = "https://fatmap.com/guidebooks/62606/10-of-lyngen&#x27;s-finest-couloirs?fmid=em"
        else:
            src= "https://fatmap.com/guidebooks/3157/classic-ski-touring-adventures-in-the-tromso-region?fmid=em"

        
        #lastly we get the current stats from the database- this is included so that we can theoretically make this code quicker by not having to run scrape each time and check if the timestamp matches today then we don't need to run the scrape code again
        stats = db.execute("SELECT location, grade, direction, type FROM avalanche WHERE location = ?", location)
        
        return render_template("data.html", location = location, stats=stats, src=src)

    else:
        # display home page again
        return render_template("home.html")




