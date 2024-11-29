import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

# Biến lưu trữ ảnh mẫu
reference_image = None

# Hàm để lưu ảnh mẫu từ camera
def capture_reference_image():
    global reference_image
    _, frame = cap.read()
    reference_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("Đã chụp ảnh mẫu")

# Hàm cập nhật khung hình từ camera và so sánh với ảnh mẫu
def update_frame():
    # Đọc khung hình từ camera
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if reference_image is not None:
        # Tính sự khác biệt giữa khung hình hiện tại và ảnh mẫu
        diff = cv2.absdiff(reference_image, gray_frame)
        
        # Ngưỡng hóa sự khác biệt để làm nổi bật các vùng khác nhau
        _, diff_threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        
        # Tìm các đường viền của các vùng khác biệt
        contours, _ = cv2.findContours(diff_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Vẽ các đường viền của các vùng khác biệt trên khung hình gốc
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 50:  # Lọc các vùng nhỏ để chỉ hiển thị khác biệt lớn
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, f"Diff: {int(area)}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    
    # Chuyển khung hình thành định dạng mà Tkinter có thể hiển thị
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)
    
    # Cập nhật hình ảnh trong giao diện Tkinter
    camera_label.imgtk = imgtk
    camera_label.configure(image=imgtk)
    camera_label.after(10, update_frame)

# Tạo cửa sổ Tkinter
root = Tk()
root.title("Nhận diện sự khác biệt so với ảnh mẫu")

# Khởi tạo camera
cap = cv2.VideoCapture(0)  # 0 là chỉ số của camera mặc định

# Tạo widget để hiển thị khung hình từ camera
camera_label = Label(root)
camera_label.pack()

# Nút để chụp ảnh mẫu
capture_button = Button(root, text="Chụp ảnh mẫu", command=capture_reference_image)
capture_button.pack()

# Bắt đầu cập nhật khung hình
update_frame()

# Chạy ứng dụng
root.mainloop()

# Giải phóng tài nguyên camera khi ứng dụng kết thúc
cap.release()
cv2.destroyAllWindows()