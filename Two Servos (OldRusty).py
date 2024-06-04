#Run  "sudo systemctl start pigpiod" in terminal before running code - if that doesn't work run "sudo systemctl restart pigpiod" instead

import pigpio
import time

# Define GPIO pins for the servos
servo_pin1 = 2  # GPIO2 (BCM numbering)
servo_pin2 = 3  # GPIO3 (BCM numbering)

# Initialize pigpio library
pi = pigpio.pi()

if not pi.connected:
    exit()

def set_angle(servo_pin, angle):
    # Convert angle to pulse width
    pulse_width = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(servo_pin, pulse_width)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servo_pin, 0)  # Stop sending the signal
import pigpio
import time

# Define GPIO pins for the servos
servo_pin1 = 2  # GPIO2 (BCM numbering)
servo_pin2 = 3  # GPIO3 (BCM numbering)

# Initialize pigpio library
pi = pigpio.pi()

if not pi.connected:import pigpio
import time

# Define GPIO pins for the servos
servo_pin1 = 2  # GPIO2 (BCM numbering)
servo_pin2 = 3  # GPIO3 (BCM numbering)

# Initialize pigpio library
pi = pigpio.pi()

if not pi.connected:
    exit()

def set_angle(servo_pin, angle):
    # Convert angle to pulse width
    pulse_width = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(servo_pin, pulse_width)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servo_pin, 0)  # Stop sending the signal

try:
    # Move the first servo to 90 degrees
    set_angle(servo_pin1, 90)
    time.sleep(1)
    
    # Move the first servo back to 0 degrees
    set_angle(servo_pin1, 0)
    time.sleep(1)
    
    # Move the second servo to 90 degrees
    set_angle(servo_pin2, 90)
    time.sleep(1)
    
    # Move the second servo back to 0 degrees
    set_angle(servo_pin2, 0)
    time.sleep(1)
    
finally:
    # Cleanup
    pi.set_servo_pulsewidth(servo_pin1, 0)
    pi.set_servo_pulsewidth(servo_pin2, 0)
    pi.stop()

    exit()

def set_angle(servo_pin, angle):
    # Convert angle to pulse width
    pulse_width = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(servo_pin, pulse_width)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servo_pin, 0)  # Stop sending the signal

try:
    # Move the first servo to 90 degrees
    set_angle(servo_pin1, 90)
    time.sleep(1)
    
    # Move the first servo back to 0 degrees
    set_angle(servo_pin1, 0)
    time.sleep(1)
    
    # Move the second servo to 90 degrees
    set_angle(servo_pin2, 90)
    time.sleep(1)
    
    # Move the second servo back to 0 degrees
    set_angle(servo_pin2, 0)
    time.sleep(1)
    
finally:
    # Cleanup
    pi.set_servo_pulsewidth(servo_pin1, 0)
    pi.set_servo_pulsewidth(servo_pin2, 0)
    pi.stop()

try:
    # Move the first servo to 90 degrees
    set_angle(servo_pin1, 90)
    time.sleep(1)
    
    # Move the first servo back to 0 degrees
    set_angle(servo_pin1, 0)
    time.sleep(1)
    
    # Move the second servo to 90 degrees
    set_angle(servo_pin2, 90)
    time.sleep(1)
    
    # Move the second servo back to 0 degrees
    set_angle(servo_pin2, 0)
    time.sleep(1)
    
finally:
    # Cleanup
    pi.set_servo_pulsewidth(servo_pin1, 0)
    pi.set_servo_pulsewidth(servo_pin2, 0)
    pi.stop()
