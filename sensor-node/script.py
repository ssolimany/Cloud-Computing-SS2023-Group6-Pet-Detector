import cv2
import torch
from pathlib import Path
from datetime import datetime
import requests
import base64
import time  # Neu hinzugefügt

# Flask backend URL
BACKEND_URL = 'http://192.168.178.66:5001'

def draw_boxes(img, detections, class_names):
    for det in detections:
        x1, y1, x2, y2, conf, class_index = map(int, det)
        class_name = class_names[class_index]
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/gruppe6/Desktop/best_aktuell.pt')
model.conf = 0.25  # confidence threshold

# Translate class indices to readable names
class_names = {0: "hamster", 1: "dog", 2: "cat"}

# Initialize camera
cap = cv2.VideoCapture(0)

try:
    while True:
        # Capture camera image
        ret, frame = cap.read()
        if not ret:
            break

        # YOLOv5 analysis
        results = model(frame)

        # Filter detections
        detections = []
        for det in results.pred[0]:
            if int(det[5]) in (0, 1, 2):  # 0: Hamster, 1: Dogs, 2: Cats
                detections.append(det)

        # If detections are present, send to Flask backend
        if len(detections) > 0:
            draw_boxes(frame, detections, class_names)
            detected_classes = [class_names[int(det[5])] for det in detections]
            confidences = [round(det[4].item(), 2) for det in detections]  # Convert tensor to Python number and round to 2 decimals
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            img_path = Path(f"{detected_classes[0]}-{timestamp}.jpg")

            cv2.imwrite(str(img_path), frame)
            
            # Read the image file as binary data
            with img_path.open("rb") as img_file:
                image_data = img_file.read()

            # Encode the image data as base64
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

            data = {
                'image_data': base64_encoded_image,
                'detection_classes': detected_classes,
                'detection_confidence_values': confidences,
                'detection_amount': len(confidences)
            }

            response = requests.post(url=f"{BACKEND_URL}/upload/jpeg", json=data)

            # Check the response status
            if response.status_code == 200:
                print("Data sent successfully.")
            else:
                print("Failed to send data. Status code:", response.status_code)

            # Print the response from the server
            print(response.text)

            # Sleep for 5 seconds
            time.sleep(5)

        else:
            print("No detections in the current frame")

        # Display the video stream
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
