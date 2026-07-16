import cv2

# Read the captured video
video = cv2.VideoCapture("sample_video.mp4")   # Replace with your video file name

# Check if the video is opened successfully
if not video.isOpened():
    print("Error: Cannot open video!")
    exit()

print("Controls:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

# Default speed (Normal)
delay = 30

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video Player", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('n'):
        delay = 30      # Normal Speed
    elif key == ord('s'):
        delay = 100     # Slow Motion
    elif key == ord('f'):
        delay = 5       # Fast Motion

video.release()
cv2.destroyAllWindows()
