from flask import render_template,request,g
from app import app
from app import db,models
from relay_control import Relay
import os
import time

#
def sprinklr(state):
	
