import cv2
from ultralytics import YOLO
import torch

url = "http://192.168.56.1:8080"
modelPath =  "Minimum Product\coco.pt"

cap = cv2.VideoCapture(url)
model = YOLO(modelPath)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret:
        # Detect objects in the frame
        results = model(frame)
        
        # Iterate over the detections and draw bounding boxes
        for _, bbox, _ in results.xyxy[0]:
            # Convert bbox coordinates to integers
            bbox = bbox.int()
            # Draw rectangle around the object
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        
        # Display the frame with bounding boxes
        cv2.imshow('frame', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()