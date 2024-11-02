import cv2
import tensorflow as tf
import numpy as np

# Load mô hình đã được huấn luyện (ví dụ, mô hình MobileNet được huấn luyện trên ImageNet)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Hàm để xử lý và dự đoán sản phẩm
def process_and_predict(image):
    # Resize hình ảnh để phù hợp với đầu vào của mô hình
    img = cv2.resize(image, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    
    # Dự đoán lớp sản phẩm
    predictions = model.predict(img)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    return decoded_predictions[0][0][1]  # Trả về tên của sản phẩm

# Khởi động camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Nhận diện sản phẩm trong khung hình
    product_name = process_and_predict(frame)
    
    # Hiển thị tên sản phẩm
    cv2.putText(frame, f"Product: {product_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Hiển thị khung hình
    cv2.imshow('Product Detection', frame)
    
    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()