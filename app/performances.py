from flask import Blueprint, request, abort

performances = Blueprint('performance', __name__)

@performances.route("/")
def status():
    return "Give Current Status"

@performances.route("/on")
def on():
    return "LED ON"

@performances.route("/off")
def off():
    return "LED OFF"
