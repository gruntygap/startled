from flask import Blueprint, request, abort
from threading import Thread

from app.leds import pixels, locker
from app.leds.led_func import rainbowCycle, fill, colorWipe

performances = Blueprint('performance', __name__)
thread = None

@performances.route("/")
def status():
	return "Give Current Status"


@performances.route("/on")
def on():
	stop_current()
	colorWipe(pixels, (255,255,255))
	# fill(pixels, (200,200,200))
	return "LED ON"


@performances.route("/off")
def off():
	stop_current()
	fill(pixels, (0,0,0))
	return "LED OFF"


@performances.route("/rainbow")
def rainbow():
	stop_current()
	global thread
	thread = Thread(target=rainbowCycle, daemon=True, args=[pixels])
	thread.start()
	return "RAINBOW"

def stop_current():
	if thread is not None:
		global thread, locker
		locker.lock = True
		thread.join()
		thread = None
		locker.lock = False
