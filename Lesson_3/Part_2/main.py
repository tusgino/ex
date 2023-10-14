# Bài tập:
# + Đọc được số ngón tay
# + Nhận 1 key từ bàn phím (x),
# + Xử lý nhận bàn tay => xác định kéo || búa || bao => Random kéo || búa || bao
# => xác định máy hoặc người chiến thắng và in lên video

# Luồng hoạt động:

# 5 => 0
# 0 => 1
# 2 => 2

# Theo cột (pc), theo hàng(user)

# 0: user win
# 1: pc win
# 2: draw

#   0 1 2
# 0 2 1 0
# 1 0 2 1
# 2 1 0 2

import cv2
import time
import os
import hand_lib as hlib
import random

video = cv2.VideoCapture(1)

video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

matrix = [
    [2, 1, 0],
    [0, 2, 1],
    [1, 0, 2]
]

def writeText(frame, text, x, y):
    cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)


def handle_player(frame, n_finger):

    switcher = {
        0: "You lose",
        1: "You win",
        2: "Draw"
    }

    if n_finger == -1:
        writeText(frame, "Invalid", 100, 100)
        return

    n_pc = random.randint(0, 2)

    image_player = listImage[n_finger]
    image_pc = listImage[n_pc]


    h_pc, w_pc, _ = image_pc.shape
    h_pl, w_pl, _ = image_player.shape

    writeText(frame, "Player", 10, 80)
    frame[100: 100 + h_pl, 10 : 10 + w_pl] = image_player
    writeText(frame, "PC", w_pl + 20, 80)
    frame[100: 100 + h_pc, w_pl + 20 : w_pl + 20 + w_pc] = image_pc

    result = matrix[n_finger][n_pc]

    result_text = switcher.get(result, "Invalid")

    writeText(frame, result_text, 10, 450)


if __name__ == "__main__":

    pathFolder = "Fingers"

    list = os.listdir(pathFolder)

    list.sort()

    listImage = []

    for file in list:
        image = cv2.imread(pathFolder + "/" + file)
        listImage.append(image)

    detector = hlib.HandDetector()

    start_time = time.time()

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame, hands_lms = detector.findHands(frame)

        end_time = time.time()
        fps = 1 / (end_time - start_time)
        start_time = end_time

        cv2.putText(frame,"FPS: " + str(int(fps)), (1280-200, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv2.imshow("Video", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

        if key == ord("x"):
            n_finger = detector.count_Fingers(hands_lms)
            print(n_finger)
            n = -1
            if n_finger == 0:
                n = 1
            elif n_finger == 2:
                n = 2
            elif n_finger == 5:
                n = 0
            handle_player(frame, n)
            cv2.imshow("Game", frame)

    video.release()