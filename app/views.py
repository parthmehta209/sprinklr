from flask import render_template
from app import app

from app import db,models
from relay_control import Relay
import os

RELAY_PIN = 14

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/turnon')
def turnon():
    if os.environ.get('TEST_NO_PI') is None:
        Relay.turnOn(RELAY_PIN)
    logEntry = models.EventLog(source="WebUI",action="TurnOn")
    db.session.add(logEntry)
    db.session.commit()
    return 'ok'

@app.route('/turnoff')
def turnoff():
    if os.environ.get('TEST_NO_PI') is None:
        Relay.turnOff(RELAY_PIN)
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
