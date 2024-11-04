import cv2
import mediapipe as mp
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

# Khởi tạo Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Stain Detection on White Paper with Mediapipe")

# Khởi tạo nhãn để hiển thị video
lbl_video = Label(root)
lbl_video.pack()

# Hàm để cập nhật video và nhận diện vết bẩn
def update_frame():
    ret, frame = cap.read()  # Đọc khung hình từ camera
    if ret:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = objectron.process(rgb_frame)

        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                    frame, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS
                )
                # Thêm nhãn vào khung hình
                cv2.putText(frame, 'Stain Detected', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl_video.imgtk = imgtk
        lbl_video.configure(image=imgtk)
    root.after(10, update_frame)  # Cập nhật khung hình sau 10ms

# Mở camera
cap = cv2.VideoCapture(0)

# Khởi tạo Mediapipe Objectron
objectron = mp_objectron.Objectron(static_image_mode=False, max_num_objects=5, min_detection_confidence=0.5, model_name='Cup')

# Bắt đầu cập nhật video
update_frame()

# Chạy ứng dụng Tkinter
root.mainloop()

# Giải phóng camera khi đóng cửa sổ
cap.release()
objectron.close()
