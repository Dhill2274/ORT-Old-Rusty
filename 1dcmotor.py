import RPi.GPIO as GPIO

import time

 

# GPIO setup

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

 

# Define GPIO pins for motor A

IN1 = 17

IN2 = 27

ENA = 18

 

# Set up GPIO pins for motor A

GPIO.setup(IN1, GPIO.OUT)

GPIO.setup(IN2, GPIO.OUT)

GPIO.setup(ENA, GPIO.OUT)

 

# Set up PWM for motor A speed control

pwmA = GPIO.PWM(ENA, 1000)

pwmA.start(100)  # Adjust this value for desired speed (0-100)

 

def forward():

  GPIO.output(IN1, GPIO.HIGH)

  GPIO.output(IN2, GPIO.LOW)

 

def backward():

  GPIO.output(IN1, GPIO.LOW)

  GPIO.output(IN2, GPIO.HIGH)

 

def stop():

  GPIO.output(IN1, GPIO.LOW)

  GPIO.output(IN2, GPIO.LOW)

 

try:

  for i in range(5):

    # Call the desired motor function here

    forward()

    time.sleep(0.2)

    stop()

    time.sleep(0.1)

    backward()

    time.sleep(0.2)

    stop()

    time.sleep(0.1)

 

except KeyboardInterrupt:

  GPIO.cleanup()