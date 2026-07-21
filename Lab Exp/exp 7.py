import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Cannot access webcam!")
    exit()

print("Controls:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

# Default delay (Normal Speed)
delay = 30

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame!")
        break

    # Display the frame
    cv2.imshow("Webcam Video", frame)

    # Wait according to the selected speed
    key = cv2.waitKey(delay) & 0xFF

    # Keyboard controls
    if key == ord('q'):
        break
    elif key == ord('n'):
        delay = 30      # Normal Speed
    elif key == ord('s'):
        delay = 100     # Slow Motion
    elif key == ord('f'):
        delay = 5       # Fast Motion

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
