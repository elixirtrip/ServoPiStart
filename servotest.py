import RPi.GPIO as GPIO
import time


class MyServo:
    """Object for servo"""

    def __init__(self, SP=17, frequency=50, rpGPIO=GPIO):
        self.servoPIN = SP
        self.frequency = frequency
        self.rpGPIO = rpGPIO.setmode(GPIO.BCM)
        self.rpGPIO = rpGPIO.setup(self.servoPIN, GPIO.OUT)
        # GPIO 17 for PWN with 50HZ
        self.p = rpGPIO.PWM(self.servoPIN, self.frequency)
        # self.p.start(2)
        # self.p.stop()

    def ServoAngle(self, y):
        self.p.ChangeDutyCycle(y)


# x = MyServo()
# try:
    # for i in range(2, 12, 2):
        # x.ServoAngle(i)
        # time.sleep(0.5)
# except KeyboardInterrupt:
    # x.p.stop()
    # x.p.cleanup()
