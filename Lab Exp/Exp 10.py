import cv2
import numpy as np
img = cv2.imread("sample.jpg")
if img is None:
    print("Error: Image not found!")
else:
    rows, cols = img.shape[:2]

    tx = 100   
    ty = 50 

    
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])

    
    moved_image = cv2.warpAffine(img, M, (cols, rows))

    
    cv2.imshow("Original Image", img)
    cv2.imshow("Moved Image", moved_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
