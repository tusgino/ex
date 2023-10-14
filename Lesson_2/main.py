import time
import cv2
import numpy as np

video = cv2.VideoCapture("Video.mp4")

delay = 1/60
while True:
    start_time = time.time()
    ret, frame = video.read()

    # Lấy kích thước của video
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if not ret:
        break

    # Vẽ đường thẳng
    cv2.line(frame, (width, 0), (0, height), (0, 0, 255), 2)

    # Vẽ hình chữ nhật (chia làm 2 tam giác vuông)
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)

    # Vẽ hình tròn
    cv2.circle(frame, (250, 250), 100, (255, 0, 0), -1)

    # Vẽ hình elip
    cv2.ellipse(frame, (500, 500), (100, 50), 45, 0, 360, (255, 255, 0), 2)

    # Vẽ đa giác

    pts = [[250, 150], [150, 250], [350, 250]]
    # Chuyển list thành numpy array
    pts_np = np.array(pts, np.int32)

    # isClosed => xác định có nối điểm cuối với điểm đầu không
    # cv2.polylines(frame, [pts_np], False, (0, 255, 255), 2)

    # Vẽ đa giác có màu
    point_fulfilled = pts_np.reshape((-1, 1, 2))
    # -1 : tự động tính số hàng
    # 1 => mỗi điểm là 1 mảng 1 chiều [x, y]
    # 2 => mỗi mảng sẽ có 2 phần tử x, y

    # [point_fulfilled] => chuyển thành list
    cv2.fillPoly(frame, [point_fulfilled], (0, 255, 255))

    # Vẽ văn bản
    font = cv2.FONT_HERSHEY_SIMPLEX
    Text = "Hello World"

    cv2.putText(frame, Text, (400, 300), font, 2, (0, 0, 0), 2)


    cv2.imshow("Video", frame)
    elapsed_time = time.time() - start_time
    sleep_time = delay - elapsed_time

    if sleep_time > 0:
        time.sleep(sleep_time)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break