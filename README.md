# Arduino-Based Computer Vision Finger Counter

## Introduction

Welcome! This project is a fun way to learn about computer vision and hardware control. You'll use your computer's camera to detect how many fingers you're holding up, and based on that, light up LEDs connected to an Arduino board. It's perfect for beginners who want to try something hands-on with coding and electronics.

Imagine showing 3 fingers to your camera, and 3 LEDs light up on your Arduino! This project combines software (Python with OpenCV) and hardware (Arduino) to make it happen.

![Project Demo](https://github.com/FreDrickMwepu/ArduinoBase_ComputerVision_Counter/assets/88320754/2c8d740c-f98a-4f18-b41a-6e98a345ede1)

## What You'll Need

Before starting, gather these items:
- **Arduino Board** (like Arduino Uno) - the brain of your hardware.
- **5 LEDs** (any color) - these will light up based on your fingers.
- **5 Resistors** (220 ohms) - to protect the LEDs from too much electricity.
- **Jumper Wires** - to connect everything.
- **Breadboard** (optional but helpful) - for easy connections.
- **USB Cable** - to connect Arduino to your computer.
- **Webcam** - most laptops have one built-in.
- **Computer** - with macOS, Windows, or Linux.

Don't worry if you've never used these before; we'll explain each step!

## Tools and Software

We'll use these tools:
- **Python**: A programming language for writing the code.
- **OpenCV**: A library for computer vision (detecting fingers).
- **PyFirmata**: Helps Python talk to Arduino.
- **CVZone**: Makes hand detection easier.
- **Arduino IDE**: Software to program the Arduino.
- **VS Code or any text editor**: To edit code.

![Tools](https://skillicons.dev/icons?i=raspberrypi,npm,opencv,vscode,git,github,arduino,pycharm)

## Step-by-Step Setup

Follow these steps carefully. If something doesn't work, check the Troubleshooting section at the end.

### 1. Install Python

Python is the language we'll use. If you don't have it:
- Go to [python.org](https://www.python.org/) and download the latest version for your OS.
- Follow the installer instructions.
- Open a terminal (on macOS, search for "Terminal" in Spotlight) and type `python3 --version`. You should see a version number like "Python 3.10.0". If not, try `python --version`.

### 2. Install Required Libraries

These are extra tools for Python. Open your terminal and run:
```
pip install opencv-python pyfirmata cvzone
```
- `pip` is Python's package installer.
- This might take a few minutes. If you get errors, make sure Python is installed correctly.

### 3. Hardware Setup

Let's connect the LEDs to your Arduino:
- Connect the positive leg (longer leg) of each LED to Arduino pins 9, 10, 11, 12, and 13 through a 220 ohm resistor.
- Connect the negative leg (shorter leg) of each LED to the GND (ground) pin on Arduino.
- Use jumper wires and a breadboard if needed.

Example: LED1 to pin 9, LED2 to pin 10, etc.

**Safety Note**: Double-check connections to avoid damaging your Arduino.

### 4. Upload Firmata Firmware to Arduino

Firmata is a protocol that lets Python control Arduino.
- Download and install the Arduino IDE from [arduino.cc](https://www.arduino.cc/en/software).
- Connect your Arduino to your computer with the USB cable.
- Open Arduino IDE.
- Go to `File > Examples > Firmata > StandardFirmata`.
- Select your Arduino board (e.g., Arduino Uno) from `Tools > Board`.
- Select the port (e.g., /dev/tty.usbmodemXXXXX) from `Tools > Port`.
- Click the Upload button (right arrow). You should see "Done uploading" in the console.

If you see errors, check your board and port selection.

### 5. Identify the Serial Port

Your computer talks to Arduino through a "port". Find yours:
- **macOS**: Open Terminal and run `ls /dev/tty.*`. Look for something like `/dev/tty.usbmodem141201`.
- **Windows**: Check Device Manager under Ports.
- **Linux**: Run `ls /dev/tty*`.

Note the port name; you'll need it in the code.

### 6. Run the Script

The script detects fingers and controls LEDs. Copy this code into a file named `controller.py`:

```python
# AUTHOR: FREDRICK MWEPU
# DATE: 13/06/2024
import cv2
import pyfirmata
from cvzone.HandTrackingModule import HandDetector

# Initialize communication with Arduino
# Replace '/dev/tty.usbmodem141201' with your actual port
comport = '/dev/tty.usbmodem141201'  
board = pyfirmata.Arduino(comport)

# Define the LED pins on the Arduino Board
led_1 = board.get_pin('d:13:o')
led_2 = board.get_pin('d:12:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:10:o')
led_5 = board.get_pin('d:9:o')

# Function to control the LEDs based on the number of fingers up
def led(fingerUp):
    # Turn off all LEDs
    if fingerUp == [0, 0, 0, 0, 0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    # Turn on the LEDs based on the number of fingers up
    elif fingerUp == [0, 1, 0, 0, 0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 0, 0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp == [1, 1, 1, 1, 1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Start the video capture
video = cv2.VideoCapture(1)

# Main loop to detect the number of fingers up
try:
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        hands, img = detector.findHands(frame)
        if hands:
            lmList = hands[0]
            fingerUp = detector.fingersUp(lmList)
            print(fingerUp)
            led(fingerUp)
            if fingerUp == [0, 0, 0, 0, 0]:
                cv2.putText(frame, 'Finger count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            elif fingerUp == [0, 1, 0, 0, 0]:
                cv2.putText(frame, 'Finger count: 1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            elif fingerUp == [0, 1, 1, 0, 0]:
                cv2.putText(frame, 'Finger count: 2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            elif fingerUp == [0, 1, 1, 1, 0]:
                cv2.putText(frame, 'Finger count: 3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            elif fingerUp == [0, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger count: 4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            elif fingerUp == [1, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger count: 5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == ord("k"):
            break
finally:
    video.release()
    cv2.destroyAllWindows()
    board.exit()
```

- Change the `comport` variable to your serial port from step 5.
- Save the file as `controller.py` in the same folder.
- Open Terminal, navigate to the folder (e.g., `cd /path/to/your/folder`), and run `python3 controller.py`.
- A window should open showing your camera feed. Hold up fingers, and watch the LEDs!

Press 'k' to stop.

## How It Works

- The camera captures video.
- OpenCV and CVZone detect your hand and count fingers.
- PyFirmata sends signals to Arduino to turn LEDs on/off.
- The screen shows the count.

## Troubleshooting

- **Python not found**: Make sure it's installed and in your PATH.
- **Library install fails**: Try `pip3` instead of `pip`, or use a virtual environment.
- **Arduino upload fails**: Check USB connection, board/port selection.
- **No LEDs lighting**: Verify connections and port in code.
- **Camera not working**: Try changing `cv2.VideoCapture(1)` to `cv2.VideoCapture(0)`.
- **Script errors**: Ensure all libraries are installed and port is correct.

If stuck, search online or ask in forums!

## Project Description

This project combines computer vision and hardware control for an interactive app. OpenCV detects fingers from webcam input, and Arduino controls LEDs accordingly. It demonstrates gesture recognition and microcontroller integration.

![Another Image](https://github.com/FreDrickMwepu/ArduinoBase_ComputerVision_Counter/assets/88320754/24b85a2f-0e13-452e-a60f-efbbc76107eb)

## Let's Connect

Follow me for more projects:
- Twitter: [@mwepufredrick](https://twitter.com/@mwepufredrick)
- LinkedIn: [fredrick mwepu](https://linkedin.com/in/fredrick mwepu)
- Facebook: [fredrick mwepu](https://fb.com/fredrick mwepu)
- Instagram: [fredrickmwepu](https://instagram.com/fredrickmwepu)
- Dribbble: [fredrick mwepu](https://dribbble.com/fredrick mwepu)
- YouTube: [fredrick mwepu](https://www.youtube.com/c/fredrick mwepu)
