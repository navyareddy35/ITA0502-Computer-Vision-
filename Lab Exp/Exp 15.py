import cv2
import numpy as np

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

src_points = np.array([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
], dtype=np.float32)

dst_points = np.array([
    [20, 80],
    [280, 40],
    [80, 320],
    [320, 300]
], dtype=np.float32)

H, mask = cv2.findHomography(src_points, dst_points, method=0)

transformed = cv2.warpPerspective(image, H, (400, 400))

cv2.imshow("Original Image", image)
cv2.imshow("DLT Transformed Image", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
