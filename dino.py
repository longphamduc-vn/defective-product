import cv2

def calculate_focus(frame):
    # Sử dụng biến đổi Laplacian để tính độ sắc nét
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def autofocus(camera_index=0):
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Không thể mở camera")
        return

    best_focus_value = 0
    best_frame = None

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            focus_value = calculate_focus(frame)
            if focus_value > best_focus_value:
                best_focus_value = focus_value
                best_frame = frame

            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    if best_frame is not None:
        cv2.imshow('Best Focused Frame', best_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Không tìm thấy khung hình tốt nhất")

if __name__ == "__main__":
    autofocus()
