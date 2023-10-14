import time
import cv2

# id tùy thuộc vào từng máy
id_camera = 1

# video = cv2.VideoCapture("Video.mp4")
video = cv2.VideoCapture(id_camera)

# Chuyển đổi 60 fps
wait_time = 1000 / 60

delay = 1 / 60 # (1/60 giây = 0.016666666666666666 giây = 16.666666666666668 ms

while True:
    start_time = time.time() # Real time

    # Giả sử đọc frame mất 5 ms
    # 1
    ret, frame = video.read()



    # Kiểm tra xem có đọc được frame không
    if not ret:
        break

    # Giả sử xử lý ảnh mất 5 ms
    # Giả sử xử lý ảnh mất 20 ms
    # Hiển thị frame
    cv2.imshow("Video Color", frame)

    # 10 ms
    # 25 ms
    elapsed_time = time.time() - start_time

    # 16.7 - 10 = 6.7 ms
    # 16.7 - 25 = -8.3 ms


    sleep_time = delay - elapsed_time

    # 6.7 > 0 => sleep 6.7 ms đảm bảo việc khoảng cách các frame là 1/60 giây
    # nếu như sleep_time < 0 thì không sleep và fps sẽ thấp hơn 60 fps
    if sleep_time > 0:
        time.sleep(sleep_time)


    # Chờ đọc phím bất kỳ với thời gian chờ là wait_time
    # key = cv2.waitKey(int(wait_time))
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Hủy tất cả các cửa sổ đang hiển thị
# Giải phóng bộ nhớ
video.release()