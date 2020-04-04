from flask import Blueprint, render_template, request, abort
from threading import Thread

from app.leds import pixels, locker
from app.leds.led_func import rainbowCycle, fill, colorWipe

performances = Blueprint('performance', __name__)
thread = None

@performances.route("/")
def status():
	return render_template('index.html')


@performances.route("/on")
def on():
	stop_current()
	global thread
	thread = Thread(target=colorWipe, daemon=True, kwargs=dict(strip=pixels, color=(127,127,127)))
	thread.start()
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
	thread = Thread(target=rainbowCycle, daemon=True, kwargs=dict(strip=pixels, iterations=-1))
	thread.start()
	return "RAINBOW"

def stop_current():
	global thread, locker
	if thread is not None:
		locker.lock = True
		thread.join()
		thread = None
		locker.lock = False
