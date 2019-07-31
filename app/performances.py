from flask import Blueprint, request, abort
from threading import Thread

from app.leds import pixels, locker
from app.leds.led_func import rainbowCycle, fill

performances = Blueprint('performance', __name__)
thread = None

@performances.route("/")
def status():
	return "Give Current Status"


@performances.route("/on")
def on():
    return "LED ON"


@performances.route("/off")
def off():
	fill(pixels, (0,0,0))
	return "LED OFF"


@performances.route("/rainbow")
def rainbow():
	global thread
	thread = Thread(target=rainbowCycle, daemon=True, args=[pixels])
	thread.start()
	return "RAINBOW"

def stop():
	global thread, locker
	locker.lock = True
	thread.join()
	locker.lock = False