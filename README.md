# Finger Counting with OpenCV and Arduino

This project integrates OpenCV and Arduino to create a system that counts the number of fingers shown to a camera and lights up the corresponding number of LEDs on a breadboard. The system uses computer vision to detect and count fingers in live footage and communicates this information to an Arduino, which then controls the LEDs.

## Components

- **Arduino Uno**
- **USB cable**
- **Breadboard**
- **Jumper wires**
- **LEDs (5)**
- **Resistors (5)**

## Setup

1. **Hardware Setup**:
    - Connect each LED to the breadboard.
    - Connect a resistor in series with each LED.
    - Connect the other end of each resistor to a digital pin on the Arduino (e.g., pins 2, 3, 4, 5, 6).
    - Connect the ground (GND) of the Arduino to the ground rail on the breadboard.
    - Ensure each LED's cathode is connected to the ground rail.

2. **Software Setup**:
    - Install the Arduino IDE.
    - Install Python and the OpenCV library.

## How It Works

1. **OpenCV Finger Counting**:
    - The system captures live footage from a camera.
    - OpenCV processes the video feed to detect the number of fingers shown.
    - The number of detected fingers is sent to the Arduino via serial communication.

2. **Arduino LED Control**:
    - The Arduino receives the finger count from the OpenCV script.
    - Based on the received count, the Arduino lights up the corresponding number of LEDs.

## Notes

- Ensure the Arduino is connected to the correct COM port.
- Adjust the OpenCV finger counting function to accurately detect fingers.
- Modify the pin numbers in the Arduino code if you connect the LEDs to different pins.

## Conclusion

This project demonstrates how to combine computer vision with microcontroller control to create interactive systems. By leveraging OpenCV for image processing and Arduino for hardware control, we can build various innovative applications.

Feel free to adjust the descriptions or details as per your specific implementation or preferences.
