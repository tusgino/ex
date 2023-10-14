import cv2

import imutils

# BGR (Blue, Green, Red)

# Đọc ảnh từ file
image = cv2.imread("01.png")

# image = cv2.imread("01.png")

# HSV
# (h, s, v)
# h: 0 - 360 (0 : màu đỏ, 120: màu xanh lá, 240: màu xanh dương)
# s: 0 - 100
# v: 0 - 100
# Hiển thị ảnh

# alias
#  BGR -> GRAY
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# Resize theo tuyệt đối (pixel)

# image_resize = cv2.resize(image, (700, 500))

# Resize theo tỉ lệv (%)
# image_resize_ratio = cv2.resize(image, dsize=None, fx=0.5, fy=0.5)

angle = {
    "0": 0,
    "45": 45,
    "90": 90,
    "180": 180,
    "270": 270
}

scale = 1.0

# Xoay ảnh
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# Tạo ma trận xoay
# scale = 1.0 => giữ nguyên kích thước ảnh
# 2x3 => 2x3
# M = cv2.getRotationMatrix2D(center, angle["180"], scale)

# Xoay ảnh
# image_rotate = cv2.warpAffine(image, M, dsize=(w, h))

#image_rotate = imutils.rotate(image, angle["180"])

cv2.imshow("Image Color", image)

# cv2.imshow("Image Rotate", image_rotate)
# cv2.imshow("Image Resize", image_resize)
# cv2.imshow("Image Resize Ratio", image_resize_ratio)
# cv2.imshow("Image Gray", image_gray)
# cv2.imshow("Image HSV", image_hsv)

# 0 -> 255 (đặt ngưỡng là 127)

# pixel có ngưỡng thấp hơn 127 thì đặt thành 0
# pixel có ngưỡng cao hơn 127 thì đặt thành 255

# Chờ đọc phím bất kỳ
cv2.waitKey(0)

# Hủy tất cả các cửa sổ đang hiển thị
cv2.destroyAllWindows()


# imread, imshow, waitKey, destroyAllWindows
