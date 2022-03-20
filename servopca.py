import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import adafruit_motor.servo
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 50
kit = ServoKit(channels=16)
servo = adafruit_motor.servo.Servo(servo_channel)
kit.servo[0].angle = 90

