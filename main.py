from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html', title = "User_Signup")

app.run()