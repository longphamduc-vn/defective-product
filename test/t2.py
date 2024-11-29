import cv2
import numpy as np

# Đọc hình mẫu
template = cv2.imread('template.jpg', cv2.IMREAD_GRAYSCALE)
template_w, template_h = template.shape[::-1]

# Khởi tạo camera
cap = cv2.VideoCapture(0)  # Thay đổi số 0 nếu cần thiết cho thiết bị của bạn

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    if not ret:
        break

    # Chuyển đổi khung hình sang thang màu xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Thực hiện so khớp mẫu 
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # Vẽ hình chữ nhật xung quanh các khu vực trùng khớp
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + template_w, pt[1] + template_h), (0, 0, 255), 2)

    # Hiển thị kết quả
    cv2.imshow('Detected', frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng bộ nhớ và đóng các cửa sổ
cap.release()
cv2.destroyAllWindows()
