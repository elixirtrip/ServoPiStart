import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWN with 50HZ
p.start(2.5)  # Initialization


class MyServo:
    """Object for servo"""

    pin = 17

    def ServoAngle(self, y):
        p.ChangeDutyCycle(y)

x = MyServo()

try:
    for i in range(2, 12, 2):
        x.ServoAngle(i)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()



