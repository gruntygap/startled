import board
import neopixel

NUM_LEDS = 300

# init 'pixels' ( WS2812b ) LEDs
pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=1.0, auto_write=False)

class Locker():
    def __init__(self, lock=False):
        self._lock = lock
    
    @property
    def lock(self):
        return self._lock

    @lock.setter
    def lock(self, lock):
        self._lock = lock

locker = Locker()
