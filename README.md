# Object-Tracking-Robo

Raspberry Pi is used to control the robot's
movements and a servo motor is used to control the orientation
of the robot's camera. By combining these technologies, the robot
can detect and track an object in its field of view, adjusting its
position and orientation to keep the object centered in the
camera's view. This project include combination of Raspberry Pi
,computer vision, and programming, and can be adapted for a
wide range of applications such as security monitoring, object
inspection, and automated navigation

The script captures frames from the camera, applies edge detection to detect the object, calculates its centroid, and moves the servo motor to track it.

<h2><b>Requirements</b></h2>

- Raspberry Pi
- Servo motor
- Camera
- Python 3
- OpenCV
- RPi.GPIO

## Installation

1. Clone the repository
2. Install the required packages:
    - `pip3 install opencv-python RPi.GPIO`
3. Run the script:
    - `python3 object_tracking.py`
