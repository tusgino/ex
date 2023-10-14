import cv2

# BGR (Blue, Green, Red)
image = cv2.imread("01.png")

# Convert to gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# cv2.THRESH_BINARY => Chiều xuôi vượt ngưỡng thì giá trị là 255, ngược lại là 0
# cv2.THRESH_BINARY_INV => Chiều ngược vượt ngưỡng thì giá trị là 0, ngược lại là 255
ret, image_threshold = cv2.threshold(image_gray, 80, 255, cv2.THRESH_BINARY)

if ret:
    cv2.imshow("Image Color", image)
    cv2.imshow("Image Threshold", image_threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")

image_threshold_adaptive = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)

cv2.imshow("Image Threshold Adaptive", image_threshold_adaptive)
cv2.waitKey(0)
