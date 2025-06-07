# import flast module
from flask import Flask, redirect, render_template

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("coachdashboard.html")

@app.route("/questionare")
def questionare():
    return render_template("questionare.html")
    
if __name__ == '__main__':  
   app.run(debug=True)