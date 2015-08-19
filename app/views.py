from flask import render_template
from app import app

from app import db,models

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/turnon')
def turnon():
    logEntry = models.EventLog(source="WebUI",action="TurnOn")
    db.session.add(logEntry)
    db.session.commit()
    return 'ok'

@app.route('/turnoff')
def turnoff():
    logEntry = models.EventLog(source="WebUI",action="TurnOff")
    db.session.add(logEntry)
    db.session.commit()
    return 'ok'

@app.route('/refreshlist')
def refreshlist():
    logs = models.EventLog.query.order_by(models.EventLog.id.desc())
    return render_template("loglist.html",logs=logs) 

@app.route('/')
def login():
    return render_template("login.html")
