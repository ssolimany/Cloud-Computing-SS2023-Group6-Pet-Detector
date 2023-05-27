import cv2
import torch
from pathlib import Path
from datetime import datetime
import requests
import base64

# Flask backend URL
BACKEND_URL = 'http://127.0.0.1:5001'

def draw_boxes(img, detections, class_names):
    for det in detections:
        x1, y1, x2, y2, conf, class_index = map(int, det)
        class_name = class_names[class_index]
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# YOLOv5-Modell laden
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/gruppe6/Desktop/best_aktuell.pt')
model.conf = 0.25  # confidence threshold

# Klassenindizes in lesbare Namen umwandeln
class_names = {0: "hamster", 1: "dog", 2: "cat"}

# Kamera initialisieren
cap = cv2.VideoCapture(0)

try:
    while True:
        # Kamerabild erfassen
        ret, frame = cap.read()
        if not ret:
            break

        # YOLOv5-Analyse
        results = model(frame)

        # Erkennungen filtern
        detections = []
        for det in results.pred[0]:
            if int(det[5]) in (0, 1, 2):  # 0: Hamster, 1: Hunde, 2: Katzen
                detections.append(det)

        # Wenn Erkennungen vorhanden sind, an Flask Backend senden
        if len(detections) > 0:
            draw_boxes(frame, detections, class_names)
            detected_classes = "-".join([class_names[int(det[5])] for det in detections])
            confidences = [det[4] for det in detections]
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            img_path = Path(f"{detected_classes}-{timestamp}.jpg")

            cv2.imwrite(str(img_path), frame)
            
            # Read the image file as binary data
            with img_path.open("rb") as img_file:
                image_data = img_file.read()

            # Encode the image data as base64
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

            data = {
                'image_data': base64_encoded_image,
                'detection_amount': detections,
                'detection_confidence_values': confidences
            }

            response = requests.post(url=f"{BACKEND_URL}/upload/jpeg", json=data)

            # Check the response status
            if response.status_code == 200:
                print("Data sent successfully.")
            else:
                print("Failed to send data. Status code:", response.status_code)

            # Print the response from the server
            print(response.text)

        else:
            print("Keine Erkennungen im aktuellen Frame")

        # Anzeige des Videostreams
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


finally:
    cap.release()
    cv2.destroyAllWindows()
