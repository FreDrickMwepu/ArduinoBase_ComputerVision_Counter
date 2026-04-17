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
- **Python 3.10.x**: The language for this project. **Use Python 3.10** (for example 3.10.12) for the best compatibility—OpenCV, PyFirmata, and CVZone are most predictable on 3.10.x. Newer versions may work but are not guaranteed. Check with `python3.10 --version` (or `python --version`) after install.
- **OpenCV**: A library for computer vision (detecting fingers).
- **PyFirmata**: Helps Python talk to Arduino.
- **CVZone**: Makes hand detection easier.
- **Arduino IDE**: Software to program the Arduino.
- **VS Code or any text editor**: To edit code.

![Tools](https://skillicons.dev/icons?i=raspberrypi,npm,opencv,vscode,git,github,arduino,pycharm)

## Step-by-Step Setup

Follow these steps carefully. **Recommended order:** install **Python 3.10.x**, create and activate a **virtual environment**, run **`pip install -r requirements.txt`**, complete the Arduino and hardware steps, then run **`python controller.py`**. If something doesn't work, check the Troubleshooting section at the end.

### 1. Install Python 3.10.x and create a virtual environment

**Use Python 3.10.x for the fewest surprises** with this stack (OpenCV, PyFirmata, CVZone). Install it from [python.org](https://www.python.org/downloads/) or your OS package manager if you do not already have it. Confirm:

```bash
python3.10 --version
```

You should see something like `Python 3.10.x`.

**Create and use a virtual environment** (keeps project packages isolated from your system Python):

| Step | Action |
|------|--------|
| Create the env | From the project folder (where `requirements.txt` lives), run: `python3.10 -m venv venv` (on Windows, if `python3.10` is not recognized, try `py -3.10 -m venv venv`) |
| **Windows** | Activate: `venv\Scripts\activate` |
| **macOS / Linux** | Activate: `source venv/bin/activate` |

After activation, your terminal usually shows `(venv)` at the start of the line. Use this same terminal for the next step.

### 2. Install dependencies from `requirements.txt`

With the virtual environment **activated**, install everything the project needs:

```bash
pip install -r requirements.txt
```

- `pip` is Python’s package installer; `-r requirements.txt` installs the pinned versions listed for this project.
- This may take a few minutes. If installation fails, confirm you are on Python 3.10.x and that the venv is active.

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

### 6. Run the application

The project includes `controller.py`, which detects fingers and drives the LEDs.

1. Open `controller.py` in your editor and set the `comport` variable to the serial port you noted in step 5 (for example `/dev/ttyUSB0` on Linux or `COM3` on Windows).
2. In a terminal, **activate your virtual environment** (same as in step 1), then go to the project folder if you are not already there.
3. Run:

```bash
python controller.py
```

On some systems the command is `python3 controller.py` instead.

- A window should open showing your camera feed. Hold up fingers, and watch the LEDs!

Press 'k' to stop.

## How It Works

- The camera captures video.
- OpenCV and CVZone detect your hand and count fingers.
- PyFirmata sends signals to Arduino to turn LEDs on/off.
- The screen shows the count.

## Troubleshooting

- **Python not found**: Install Python 3.10.x and ensure it is on your PATH. On Windows you may use the `py` launcher: `py -3.10`.
- **Wrong Python version**: Prefer **3.10.x**; recreate the venv with `python3.10 -m venv venv` after installing 3.10.
- **Library install fails**: Activate the virtual environment first, then run `pip install -r requirements.txt` again. Try `python -m pip install -r requirements.txt` if `pip` is not found.
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
