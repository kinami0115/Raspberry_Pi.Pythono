#LED1 : DATE IN
#LED2 : 5V+
#LED3 : GND
#LED4 : DATE OUT

import neopixel, time ,sys

LED_COUNT = 5
LED_PIN = 18
LED_BRIGHTNESS = 255
LED_CHANNEL = 0

def SetColor(strip, num, color, milli_sec):
    for i in range(milli_sec):
        strip.setPixelColor(num,color)
        strip.show()
        time.sleep(0.0001)

strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, 800000, 10, False, LED_BRIGHTNESS,
LED_CHANNEL, 1050624)
strip.begin()

def OneByOne():
    for i in range(LED_COUNT):
        if i % 3 ==1:
            for j in range(256):
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1) #Blue ~Red
            for j in range(256):
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1) #Red  ~Green
            for j in range(256):
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1) #Green ~ Blue
        if i % 3 ==2:
            for j in range(256):
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1) #Red  ~Green
            for j in range(256):
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1) #Green ~ Blue
            for j in range(256):
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1) #Blue ~Red
        if i % 3 ==0:
            for j in range(256):
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1) #Green ~ Blue
            for j in range(256):
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1) #Blue ~Red
            for j in range(256):
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1) #Red  ~Green

def All():
    for j in range(256):
        for i in range(LED_COUNT):
            if i%3 == 1:
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1) #Blue ~ Red
            if i%3 == 2:
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1) #Red ~ Green
            if i%3 == 0:
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1) #Green ~ Blue
    for j in range(256):
        for i in range(LED_COUNT):
            if i%3 == 1:
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1) #Red ~ Green
            if i%3 == 2:
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1) #Green ~ Blue
            if i%3 == 0:
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1) #Blue ~ Red
    for j in range(256):
        for i in range(LED_COUNT):
            if i%3 == 1:
                SetColor(strip, i, neopixel.Color(0, 255 - j, j), 1) #Green ~ Blue
            if i%3 == 2:
                SetColor(strip, i, neopixel.Color(j, 0, 255 - j), 1) #Blue ~ Red
            if i%3 == 0:
                SetColor(strip, i, neopixel.Color(255 - j, j, 0), 1) #Red ~ Green

try:
    while True:
        All()

        for i in range(LED_COUNT) :
            SetColor(strip, i, neopixel.Color(0, 0, 0), 1) #Black(off)

        OneByOne()

except:
    print("\n end")

    for i in range(LED_COUNT):
        SetColor(strip, i, neopixel.Color(0, 0, 0), 1) #Black(off)

    sys.exit(0)
    
                
                
