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

    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWN with 50HZ
    p.start(2)  # Initialization

    def ServoAngle(self, y):
        self.p.ChangeDutyCycle(y)

x = MyServo()

try:
    for i in range(2, 12, 2):
        x.ServoAngle(i)
        time.sleep(0.5)
except KeyboardInterrupt:
    x.p.stop()
    GPIO.cleanup()



