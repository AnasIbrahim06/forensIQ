from flask import* 
from database import*

court=Blueprint("court",__name__)


#court homepage

@court.route("/court_home")
def court_homepage():
    return render_template("court_home.html")


#request evidence

@court.route("/request_evidence")
def request_evidence():
    return render_template("request_evidence(C).html")