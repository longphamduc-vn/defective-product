import cv2
import numpy as np

def capture_images(device_index, num_images):
    cap = cv2.VideoCapture(device_index)
    images = []

    for i in range(num_images):
        ret, frame = cap.read()
        if ret:
            images.append(frame)
            cv2.imshow('Capturing Image', frame)
            cv2.waitKey(1000)  # Dừng 1 giây giữa mỗi ảnh để bạn có thời gian di chuyển camera
        else:
            print(f"Failed to capture image {i+1}")

    cap.release()
    cv2.destroyAllWindows()
    return images

def stitch_images(images):
    stitcher = cv2.Stitcher_create()
    status, pano = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        return pano
    else:
        print("Stitching failed")
        return None

def main():
    device_index = 0  # Thay đổi theo thiết bị camera của bạn
    num_images = 20   # Số lượng ảnh bạn muốn chụp

    images = capture_images(device_index, num_images)
    if images:
        panorama = stitch_images(images)
        if panorama is not None:
            cv2.imshow('Panorama', panorama)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite('panorama.jpg', panorama)
        else:
            print("Failed to create panorama")
    else:
        print("No images captured")

if __name__ == "__main__":
    main()
