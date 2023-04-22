import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

# Setup GPIO pins
GPIO.setmode(GPIO.BOARD)
servo_pin = 12
GPIO.setup(servo_pin, GPIO.OUT)

# Initialize servo
servo = GPIO.PWM(servo_pin, 50)
servo.start(7.5)

# Set up camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Object detection
def detect_object(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection to detect edges
    edges = cv2.Canny(blur, 50, 150)

    # Find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    max_contour = max(contours, key=cv2.contourArea)

    # Find the centroid of the largest contour
    M = cv2.moments(max_contour)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    # Draw a circle at the centroid
    cv2.circle(frame, (cx, cy), 10, (0, 255, 0), 2)

    return cx, cy

# Servo control
def move_servo(cx, cy):
    if cx is not None and cy is not None:
        error = cx - 320
        angle = error * 0.1
        duty_cycle = angle / 18.0 + 7.5
        servo.ChangeDutyCycle(duty_cycle)

# Main loop
while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Detect object and get centroid
    cx, cy = detect_object(frame)

    # Move servo to track object
    move_servo(cx, cy)

    # Display frame
    cv2.imshow("Object Tracking", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()
