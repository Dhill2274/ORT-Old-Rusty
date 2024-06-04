import pigpio
import time

servo_pin = 2  # GPIO2 (BCM numbering)
pi = pigpio.pi()

if not pi.connected:
    exit()

def set_angle(angle):
    # Convert angle to pulse width
    pulse_width = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(servo_pin, pulse_width)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(servo_pin, 0)  # Stop sending the signal

try:
    # Move the servo to 90 degrees
    set_angle(90)
    time.sleep(0.05)
    
    # Move the servo back to 0 degrees
    set_angle(0)
    time.sleep(1)
    
finally:
    # Cleanup
    pi.set_servo_pulsewidth(servo_pin, 0)
    pi.stop()