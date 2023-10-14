import cv2
import mediapipe as mp


class HandDetector:
    # Constructor (khởi tạo)
    def __init__(self):
        # mpHands => mediapipe hands
        self.mpHands = mp.solutions.hands
        # Khởi tạo bộ phát hiện tay
        self.hands = self.mpHands.Hands()
        # Khởi tạo bộ vẽ tay
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, image):
        # Chuyển ảnh sang RGB
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Xử lý ảnh
        results = self.hands.process(imgRGB)

        hands_lms = []

        # Nếu có kết quả
        # print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            # Với mỗi kết quả
            for hand_landmarks in results.multi_hand_landmarks:
                # Vẽ các điểm đốt ngón tay
                self.mpDraw.draw_landmarks(image, hand_landmarks, self.mpHands.HAND_CONNECTIONS)

            # Lấy bàn tay đầu tiên xuất hiện
            first_hand = results.multi_hand_landmarks[0]

            # height, width, channels(số kênh của ảnh)
            # rgb => 3 kênh
            # cmyk => 4 kênh
            # rgba => 4 kênh (a: alpha)
            h, w, c = image.shape

            for id, lm in enumerate(first_hand.landmark):
                # lm.x => 0 => 1
                # lm.y => 0 => 1
                # Tọa độ của điểm đốt ngón tay
                real_x = int(lm.x * w)
                real_y = int(lm.y * h)
                # Thêm vào danh sách phía sau (append)
                # [[id, real_x, real_y], [id, real_x, real_y], ...]
                hands_lms.append([id, real_x, real_y])
        return image, hands_lms

    def count_Fingers(self, hands_lms):
        finger_start_index = [4, 8, 12, 16, 20]
        finger_end_index = [3, 6, 10, 14, 18]

        n_finger = 0

        if len(hands_lms) != 0:
            if hands_lms[finger_start_index[0]][1] < hands_lms[finger_end_index[0]][1]:
                n_finger += 1

            for i in range(1, 5):
                # print(i)
                if (hands_lms[finger_start_index[i]][2] < hands_lms[finger_end_index[i]][2]):
                    n_finger += 1
            return n_finger
        else:
            return 0


