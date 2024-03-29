import RPi.GPIO as GPIO

LED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED, 100)
pwm.start(0)

try:
	while True:
		pwm.ChangeDutyCycle(50)
except:
	pwm.stop()
	GPIO.cleanup()
