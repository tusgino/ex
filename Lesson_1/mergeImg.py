import cv2
import os
import numpy as np


def merge_transparent_images_vertically_from_folder(folder_path, output_path):
    # Lấy danh sách tất cả các tệp trong thư mục
    image_files = [f for f in os.listdir(folder_path) if
                   os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.png')]

    # Đọc tất cả các ảnh
    images = []
    for image_file in image_files:
        img = cv2.imread(os.path.join(folder_path, image_file), cv2.IMREAD_UNCHANGED)

        # Nếu ảnh chỉ có 3 kênh, thêm kênh alpha
        if img.shape[2] == 3:
            alpha_channel = np.ones(img.shape[:2], dtype=img.dtype) * 255
            img = cv2.merge((img, alpha_channel))

        images.append(img)

    # Xác định kích thước tổng thể của ảnh kết quả
    max_width = max(img.shape[1] for img in images)
    total_height = sum(img.shape[0] for img in images)

    # Tạo ảnh mới với kích thước đã xác định và nền trong suốt
    merged_image = np.zeros((total_height, max_width, 4), dtype=np.uint8)

    # Ghép các ảnh lại với nhau theo chiều dọc
    y_offset = 0
    for img in images:
        merged_image[y_offset:y_offset + img.shape[0], :img.shape[1]] = img
        y_offset += img.shape[0]

    # Lưu ảnh kết quả
    cv2.imwrite(output_path, merged_image)


# Sử dụng hàm
folder_path = 'MAP'  # Thay đổi đường dẫn này thành đường dẫn của bạn
output_path = 'merged_transparent_image_vertical.png'
merge_transparent_images_vertically_from_folder(folder_path, output_path)
