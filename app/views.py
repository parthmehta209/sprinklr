from flask import render_template,request,g
from app import app
from app import db,models
from relay_control import Relay
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler

RELAY_PIN = 14
scheduler = None
job = None
task_count = 0
NUM_TASK_RUNS = 4
WATERING_INTERVAL = 5
INTERVAL_BETWN_WATER_HR = 6

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/turnon')
def turnon(eventSrc=None):
    if os.environ.get('TEST_NO_PI') is None:
        Relay.turnOn(RELAY_PIN)
    if eventSrc is 'Timer':
        logEntry = models.EventLog(source="Timer",action="TurnOn")
    else:
        logEntry = models.EventLog(source="WebUI",action="TurnOn")
    db.session.add(logEntry)
    db.session.commit()
    return 'ok'

@app.route('/turnoff')
def turnoff(eventSrc=None):
    if os.environ.get('TEST_NO_PI') is None:
        Relay.turnOff(RELAY_PIN)
    if eventSrc is 'Timer':
        logEntry = models.EventLog(source="Timer",action="TurnOff")
    else:
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

@app.route('/timeron')
def timer():
    global scheduler
    global job
    if scheduler is not None:
        job = scheduler.add_job(watering_task,'interval',hours=INTERVAL_BETWN_WATER_HR)
    else: 
        scheduler = BackgroundScheduler()
        job = scheduler.add_job(watering_task,'interval',hours=INTERVAL_BETWN_WATER_HR)
        scheduler.start()
    return 'ok'

def watering_task():
    global task_count
    global scheduler
    global job
    task_count += 1
    turnon('Timer')
    time.sleep(WATERING_INTERVAL)
    turnoff('Timer')
    
    if task_count >= NUM_TASK_RUNS:
        task_count=0
        job.remove()
