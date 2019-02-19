import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
    import FakeRPi.GPIO as GPIO
import time


class MyServo:
    """Object for servo"""
    def __init__(self, SP=17, frequency=50, GPIO=GPIO.setmode(GPIO.BCM)):
        self.servoPIN = SP
        self.frequency = frequency
        self.GPIO = GPIO.setup(self.servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(self.servoPIN, self.frequency).start(2)  # GPIO 17 for PWN with 50HZ

    def ServoAngle(self, y):
        self.p.ChangeDutyCycle(y)

x = MyServo()
x.servoPIN = 17

try:
    for i in range(2, 12, 2):
        x.ServoAngle(i)
        time.sleep(0.5)
except KeyboardInterrupt:
    x.p.stop()
    x.GPIO.cleanup()
