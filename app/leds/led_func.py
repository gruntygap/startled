from app.leds import NUM_LEDS, locker
import time

def fill(strip, color):
    strip.fill(color)
    strip.show()

def colorWipe(strip, color, wait_ms=10, rate=1):
    """Wipe color across display a pixel at a time."""
    for i in range(int(NUM_LEDS / rate)):
        for j in range(rate):
            strip[(i*rate) + j] = color
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
    for j in range(256*iterations):
        for i in range(strip.n):
            strip[i] = wheel((int(i * 256 / strip.n) + j) % 255)
        if locker.lock:
            return
        strip.show()
        time.sleep(wait_ms/1000.0)

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
