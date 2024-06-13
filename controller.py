# AURTHOR: FREDRICK MWEPU
# DATE: 13/06/2024
import cv2
import pyfirmata
from cvzone.HandTrackingModule import HandDetector

# Initialize communication with Arduino
# Replace '/dev/tty.usbmodem141201' with the correct port for your system, e.g., '/dev/tty.usbmodemXXXXX' 
comport = '/dev/tty.usbmodem141201'  
board = pyfirmata.Arduino(comport)

# Define the LED pins on the arduino Board
led_1 = board.get_pin('d:13:o')
led_2 = board.get_pin('d:12:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:10:o')
led_5 = board.get_pin('d:9:o')

# Function to control the LEDs based on the number of fingers up
def led(fingerUp):
    // Turn off all LEDs
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
    # Turn on the LEDs based on the number of fingers up
    elif fingerUp == [0, 1, 1, 0, 0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    # Turn on the LEDs based on the number of fingers up
    elif fingerUp == [0, 1, 1, 1, 0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    # Turn on the LEDs based on the number of fingers up
    elif fingerUp == [0, 1, 1, 1, 1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    # Turn on the LEDs based on the number of fingers up
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
        # Break the loop if no frame is captured
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        hands, img = detector.findHands(frame)
        # Get the list of fingers up
        if hands:
            lmList = hands[0]
            fingerUp = detector.fingersUp(lmList)

            
            # Display the number of fingers up on the screen
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

        # Display the frame
        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == ord("k"):
            break
finally:
    video.release()
    cv2.destroyAllWindows()
    board.exit()
