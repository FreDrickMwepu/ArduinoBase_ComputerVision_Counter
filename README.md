# Arduino Base ComputerVision Counter

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

## Usage

1. **Upload the Arduino Code**:
    ```cpp
    void setup() {
        Serial.begin(9600);
        for (int i = 2; i <= 6; i++) {
            pinMode(i, OUTPUT);
        }
    }

    void loop() {
        if (Serial.available() > 0) {
            int fingers = Serial.parseInt();
            for (int i = 2; i <= 6; i++) {
                if (i - 1 <= fingers) {
                    digitalWrite(i, HIGH);
                } else {
                    digitalWrite(i, LOW);
                }
            }
        }
    }
    ```

2. **Run the OpenCV Script**:
    ```python
    import cv2
    import serial
    import time

    # Set up serial communication
    ser = serial.Serial('COM3', 9600)
    time.sleep(2)  # Wait for the serial connection to initialize

    def count_fingers(frame):
        # Implement finger counting logic using OpenCV
        # This is a placeholder implementation
        # Replace with actual finger detection code
        return 3  # Assume 3 fingers are detected for this example

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        fingers = count_fingers(frame)
        ser.write(str(fingers).encode())

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ser.close()
    ```

## Notes

- Ensure the Arduino is connected to the correct COM port.
- Adjust the OpenCV finger counting function to accurately detect fingers.
- Modify the pin numbers in the Arduino code if you connect the LEDs to different pins.

## Conclusion

This project demonstrates how to combine computer vision with microcontroller control to create interactive systems. By leveraging OpenCV for image processing and Arduino for hardware control, we can build various innovative applications.

---

Feel free to adjust the descriptions or details as per your specific implementation or preferences.
