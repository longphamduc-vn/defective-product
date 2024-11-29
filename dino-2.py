import cv2
import time
import numpy as np

def is_light_on(frame, threshold=100):
    # Chuyển đổi khung hình sang màu xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Tính toán độ sáng trung bình của khung hình
    mean_brightness = np.mean(gray)
    return mean_brightness > threshold

def capture_when_light_is_on(camera_index=0, save_path='captured_image.jpg'):
    # Khởi tạo camera
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Không thể mở camera")
        return

    print("Đang chờ đèn sáng...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không thể nhận khung hình (hết stream?). Thoát...")
            break

        if is_light_on(frame):
            print("Đèn đã sáng! Chụp ảnh...")
            cv2.imwrite(save_path, frame)
            print(f"Ảnh đã được lưu tại {save_path}")
            break

        # Hiển thị khung hình
        cv2.imshow('frame', frame)

        # Nhấn 'q' để thoát
        if cv2.waitKey(1) == ord('q'):
            break

    # Giải phóng camera và đóng cửa sổ
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_when_light_is_on()
