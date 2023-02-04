from flask import Flask, render_template,request, redirect, url_for, flash,get_flashed_messages
from datetime import datetime
from model import db, accounts

app = Flask(__name__)
app.config['SECRET_KEY'] = "lhdsavfhuaio13"

username = "Unknown";

@app.route("/",methods=["GET","POST"])
def welcome():
    if request.method == "POST":
        send = {"name": username,"message": request.form['lname']}
        if len(send["name"]) > 2:
            db.append(send)
        return redirect(url_for('welcome'))
    else:
        return render_template("welcome.html",db=db,name="satvik",message = "hello")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        send = {"name": request.form['fname'], "message": request.form['lname']}
        for x in accounts:
            if x["username"] == request.form['fname'] and x["password"] == request.form['lname']:
                global username
                username = request.form['fname']
                flash('You were successfully logged in','success')
            else:
                flash('Incorrect username or password','error')

        return redirect(url_for('welcome'))
    else:
        return render_template("login.html", db=db)

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        y = 0
        send = {"username": request.form['fname'], "password": request.form['lname']}
        for x in accounts:
            if x["username"] == request.form['fname']:
                y = y + 1
        if y == 0:
            accounts.append(send)
        return redirect(url_for('welcome'))
    else:
        return render_template("signup.html", db=db)

@app.route("/logout",methods=["GET","POST"])
def logout():
    global username
    username = "Unknown"
    return redirect(url_for('welcome'))
