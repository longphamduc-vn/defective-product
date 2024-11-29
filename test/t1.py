import cv2

# Khởi tạo camera
cap = cv2.VideoCapture(0)  # Số 0 có thể thay đổi tùy thuộc vào thiết bị của bạn

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()

    if not ret:
        break

    # Chuyển đổi hình ảnh sang thang màu xám
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Sử dụng bộ phát hiện biên dạng
    edges = cv2.Canny(gray, 50, 150)

    # Hiển thị hình ảnh gốc và hình ảnh sau xử lý
    cv2.imshow('Original', frame)
    cv2.imshow('Edges', edges)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Giải phóng bộ nhớ và đóng các cửa sổ
cap.release()
cv2.destroyAllWindows()
