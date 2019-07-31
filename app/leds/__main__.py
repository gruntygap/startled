'''
Script for testing the different animations without
running the webserver and hitting the various endpoints
'''
from app.leds.led_func import colorWipe, theaterChase, rainbowCycle, rainbow, theaterChaseRainbow
from app.leds import pixels

try:
    while True:
        # print ('Color wipe animations.')
        colorWipe(pixels, (255, 0, 0), rate=1)  # Red wipe
        colorWipe(pixels, (0, 255, 0), rate=1)  # Blue wipe
        colorWipe(pixels, (0, 0, 255), rate=1)  # Green wipe
        # # print ('Theater chase animations.')
        theaterChase(pixels, (127, 127, 127))  # White theater chase
        theaterChase(pixels, (127,   0,   0))  # Red theater chase
        theaterChase(pixels, (  0,   0, 127))  # Blue theater chase
        # # print ('Rainbow animations.')
        rainbow(pixels, wait_ms=1)
        rainbowCycle(pixels)
        theaterChaseRainbow(pixels)

except KeyboardInterrupt:
    colorWipe(pixels, (0,0,0), 1, rate=10)
