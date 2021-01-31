from app.leds import NUM_LEDS, locker
import time

HSVColor = [0, 4, 8, 13, 17, 21, 25, 30,
        34, 38, 42, 47, 51, 55, 59, 64, 68,
        72, 76, 81, 85, 89, 93, 98, 102, 106,
        110, 115, 119, 123, 127, 132, 136, 140,
        144, 149, 153, 157, 161, 166, 170, 174,
        178, 183, 187, 191, 195, 200, 204, 208,
        212, 217, 221, 225, 229, 234, 238, 242,
        246, 251, 255]

def fill(strip, color):
    strip.fill(color)
    strip.show()

def colorWipe(strip, color, wait_ms=10, rate=1):
    """Wipe color across display a pixel at a time."""
    for i in range(int(NUM_LEDS / rate)):
        for j in range(rate):
            strip[(i*rate) + j] = color
        if locker.lock:
            return
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, NUM_LEDS, 3):
                strip[i+q] = color
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, NUM_LEDS, 3):
                strip[i+q] = 0

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.n):
            strip[i] = wheel((i+j) % 255)
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    repeat = False
    if iterations is -1:
       iterations = 1
       repeat = True
    while True:
        for j in range(256*iterations):
            for i in range(strip.n):
                strip[i] = wheel((int(i * 256 / strip.n) + j) % 255)
            if locker.lock:
                return
            strip.show()
            time.sleep(wait_ms/1000.0)
        if repeat is False:
            break

def staticRainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    repeat = False
    if iterations is -1:
       iterations = 1
       repeat = True
    while True:
        for k in range(360):
            # k is angle
            if k < 60:
                strip.fill((255, HSVColor[k], 0))
            elif k < 120:
                strip.fill((HSVColor[120-k], 255, 0))
            elif k < 180:
                strip.fill((0, 255, HSVColor[k-120]))
            elif k < 240:
                strip.fill((0, HSVColor[240-k], 255))
            elif k < 300:
                strip.fill((HSVColor[k-240], 0, 255))
            else:
                strip.fill((255, 0, HSVColor[360-k]))
            strip.show()
            if locker.lock:
                return
            time.sleep(wait_ms/1000.0)
        if repeat is False:
            break

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.n, 3):
                strip[i+q] = wheel((i+j) % 255)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.n, 3):
                strip[i+q] = 0
