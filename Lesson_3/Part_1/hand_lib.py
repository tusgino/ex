import cv2
import mediapipe as mp

class HandDetector:
    def  __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, image):
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        hands_lms = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(image, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
            first_hand = results.multi_hand_landmarks[0]
            h, w, c = image.shape
            for id, lm in enumerate(first_hand.landmark):
                real_x = int(lm.x * w)
                real_y = int(lm.y * h)
                hands_lms.append([id, real_x, real_y])
        return image, hands_lms

    def count_Fingers(self, hands_lms):
        if (hands_lms == []):
            return -1
        finger_start_index = [4, 8, 12, 16, 20]
        finger_end_index = [3, 6, 10, 14, 18]
        n_finger = 0
        if len(hands_lms) != 0:
            if hands_lms[finger_start_index[0]][1] < hands_lms[finger_end_index[0]][1]:
                n_finger += 1
            for i in range(1, 5):
                if (hands_lms[finger_start_index[i]][2] < hands_lms[finger_end_index[i]][2]):
                    n_finger += 1
        return n_finger

