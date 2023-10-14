import os
import time
import cv2
import hand_lib as hlib

video = cv2.VideoCapture(1)

pathFolder = "Fingers"

list = os.listdir(pathFolder)

list.sort()
# 0.png 1.png 2.png 3.png 4.png 5.png
# 0 1 2 3 4 5

listImage = []

for file in list:
    image = cv2.imread(pathFolder + "/" + file)
    # cv2.imshow(pathFolder + "/" + file, image)
    print(pathFolder + "/" + file)
    listImage.append(image)

print(listImage[0].shape)

start_time = 0

detector = hlib.HandDetector()

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame, hands_lms = detector.findHands(frame)

    n_finger = detector.count_Fingers(hands_lms)

    print(n_finger)

    # print(hands_lms)

    imageHand = listImage[n_finger]

    h, w, c = imageHand.shape

    frame[0:h, 0:w] = imageHand

    end_time = time.time()
    # frame per second
    fps = 1 / (end_time - start_time)
    start_time = end_time

    # print(fps)

    cv2.putText(frame,"FPS: " + str(int(fps)), (width - 200, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
