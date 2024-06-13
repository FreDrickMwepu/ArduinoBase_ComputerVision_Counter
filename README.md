### Project Summary

This project integrates OpenCV for hand gesture detection and PyFirmata to control LEDs connected to an Arduino based on the detected gestures. The goal is to turn on or off the LEDs according to the number of fingers detected by the camera.

![Spectacular Allis](https://github.com/FreDrickMwepu/ArduinoBase_ComputerVision_Counter/assets/88320754/2c8d740c-f98a-4f18-b41a-6e98a345ede1)

### Installation Steps

1. **Install Python**:
   - Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. **Install Required Libraries**:
   - Open a terminal or command prompt and run the following commands to install the necessary libraries:
     
     ```sh
     pip install opencv-python pyfirmata cvzone
     ```

3. **Upload Firmata Firmware to Arduino**:
   - Connect your Arduino to your computer.
   - Open the Arduino IDE.
   - Go to `File > Examples > Firmata > StandardFirmata`.
   - Select your Arduino board and port from the `Tools` menu.
   - Upload the sketch to your Arduino.

4. **Identify the Serial Port**:
   - **macOS**:
     ```sh
     ls /dev/tty.*
     ```
   - **Linux**:
     ```sh
     ls /dev/tty*
     ```
   - Look for entries like `/dev/tty.usbmodemXXXXX` or `/dev/ttyUSB0`.

5. **Run the Combined Script**:
   - Replace `'/dev/tty.usbmodemXXXXX'` with your actual port in the script.
   - Save the following combined script as `controller.py`:

6. **Run the Script**:
   - Ensure your Arduino is connected and the correct port is specified.
   - Run the script:
     ```sh
     python3 controller.py
     ```

### Project Description

This project combines computer vision and hardware control to create an interactive application. Using OpenCV, it detects the number of fingers shown to a webcam. Based on the number of detected fingers, it controls LEDs connected to an Arduino. The project showcases the integration of computer vision for gesture recognition and microcontroller control for physical outputs.
