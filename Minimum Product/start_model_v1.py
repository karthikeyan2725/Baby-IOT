import cv2
from ultralytics import YOLO
import torch


url = "rtsp://192.168.124.7:8554/stream"
modelPath =  "Minimum Product\coco.pt"

cap = cv2.VideoCapture(url)

model = YOLO(modelPath)

color = (255, 0, 0)

# model.info()

while(cap.isOpened()):

    # read returns if frame is returned, and frame is nparray
    ret, frame = cap.read()

    result = model(frame)

    boxes = result[0].boxes.xyxy.tolist()
    
    classes = result[0].boxes.cls.tolist()

    names = result[0].names

    confidences = result[0].boxes.conf.tolist()

    # Iterate through the results
    boxedFrame = frame.copy()
    for box, cls, conf in zip(boxes, classes, confidences):
        x, y, width, height = [int(x) for x in box]
        confidence = conf
        detected_class = cls
        name = names[int(cls)]
        boxedFrame = cv2.rectangle(boxedFrame, (x, y), (x + width, y + height), color, thickness=2)

    cv2.imshow('output', boxedFrame)
    if cv2.waitKey(20) & 0xFF == ord('q'): #ord('q') must be 113
        break

cap.release()
cv2.destroyAllWindows()
