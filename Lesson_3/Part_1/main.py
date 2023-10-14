import os
import time
import cv2
import hand_lib as hlib
import random



def randompc():
    return random.randint(0, 2)

def writeText(frame, text, x, y, color):
    if color == None or color == "Green":
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    if color == "Red":
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
    if color == "Blue":
        cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

def handleplayer(v_frame, n_fingers):

    switcher = {
        0: "You Lose",
        1: "You Win",
        2: "Draw"
    }

    if n_fingers == -1:
        writeText(frame, "Invalid", 100, 100, "Red")
        return


    n_pc = randompc()

    image_pc = listImage[n_pc]
    image_player = listImage[n_fingers]



    h_pc, w_pc, c = image_pc.shape
    h_pl, w_pl, c = image_player.shape

    writeText(frame, "You", 10, 80, "Green")
    writeText(frame, "PC", w_pl + 20, 80, "Red")
    v_frame[100:100 + h_pl, 10:10 + w_pl] = image_player
    v_frame[100:100 + h_pc, w_pl+20: w_pl + 20 + w_pc] = image_pc


    result = "Draw"

    # Array 2D
    # row: user
    # col: pc
    # 0: user win
    # 1: pc win
    # 2: draw

    matrix = [[2, 1, 0], [0, 2, 1], [1, 0, 2]]

    result = matrix[n_fingers][n_pc]

    print(n_fingers, n_pc)
    print(result)

    result_str = switcher.get(result, "Invalid")

    writeText(frame, result_str, 10, 400, "Blue")


if __name__ == "__main__":

    video = cv2.VideoCapture(1)

    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    pathFolder = "Fingers"

    list = os.listdir(pathFolder)

    list.sort()

    listImage = []

    for file in list:
        image = cv2.imread(pathFolder + "/" + file)
        print(pathFolder + "/" + file)
        listImage.append(image)

    start_time = 0
    detector = hlib.HandDetector()

    while True:
        ret, frame = video.read()

        if not ret:
            break

        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        frame, hands_lms = detector.findHands(frame)

        # n_finger = detector.count_Fingers(hands_lms)

        end_time = time.time()

        fps = 1 / (end_time - start_time)

        start_time = end_time

        cv2.putText(frame, "FPS: " + str(int(fps)), (width - 200, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

        if key == ord(' '):
            n_finger = detector.count_Fingers(hands_lms)
            n = -1
            if n_finger == 5:
                n = 0
            elif n_finger == 0:
                n = 1
            elif n_finger == 2:
                n = 2

            handleplayer(frame, n)
            cv2.imshow("Game", frame)

    video.release()