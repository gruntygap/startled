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


# TODO: One day make this a POST request, it's only right. (i think)
@performances.route("/static")
def static():
	r = request.args.get('r', default = 255, type = int)
	g = request.args.get('g', default = 255, type = int)
	b = request.args.get('b', default = 255, type = int)
	l = request.args.get('l', default = 0.5, type = float)
	if (r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0 or l > 1.0 or l < 0.0):
 		return "Improper Color", 400
	stop_current()
	fill(pixels, (int(r*l),int(g*l),int(b*l)))
	return "LED making color.."


@performances.route("/rainbow")
def rainbow():
        speed = request.args.get('speed', default = 20, type = int)
        if (speed < 1 or speed > 1000):
                return "Improper Speed", 400
        stop_current()
        global thread
        thread = Thread(target=rainbowCycle, daemon=True, kwargs=dict(strip=pixels, wait_ms=speed, iterations=-1))
        thread.start()
        return "RAINBOW"


def stop_current():
	global thread, locker
	if thread is not None:
		locker.lock = True
		thread.join()
		thread = None
		locker.lock = False
