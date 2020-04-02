# startled
Files that are run by a small processing unit, to render light from a string of LEDs.i

## Creating the environment and running the app.
Starting with the most important part of setting up a new app, the environment:
```python3 -m venv <path-to-env>```
```source <path-to-env>/bin/activate```
```sudo python3 run.py```
This is just how I had to do it, with a different build of python, someone might have a different experience. For some reason, it has issue with using simply ```sudo python run.py```
Furthermore, turns out that using sudo just utilizes your local build and not your env, so maybe use something like:
```sudo /<relative-path-to-env>/bin/python run.py```
Another important thing to note is that you have to use sudo to access the rpi pins on the raspberry pi (with the python neopixel package). [HOPING TO PORT THIS TO ARDUINO]

## Current Setup:

Python 3.5.3

[Lightstrip](https://www.amazon.com/gp/product/B01CDTEG1O/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) (Purchased from Amazon.com)

[Power Supply](https://www.amazon.com/gp/product/B06XK2DDW4/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) (Purchased from Amazon.com)

Raspberry Pi 3B (Purchased from ???, Microcenter???)

Assorted Wires and ??SCOTCH TAPE?? (Purchased from ???, Microcenter???)

