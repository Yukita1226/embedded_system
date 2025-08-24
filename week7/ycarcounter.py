#car capture yolo

import cv2
from ultralytics import YOLO
model = YOLO('/home/pi/OpenCV_File/data/yolov8n.pt', verbose=False)
video_path = "/home/pi/OpenCV_File/video/ThaiTraffic04_480.mp4"
roiX,roiY,roiW,roiH = 10, 150, 280, 300
frame_kStep, frame_count = 8, 0
cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    frame_count += 1
    success, mainFrame = cap.read()
    if success:
        if frame_count % frame_kStep == 0:
            frame = mainFrame[roiY:roiY+roiH, roiX:roiX+roiW]
results = model(frame, conf=0.55, verbose=True)
annotated_frame = results[0].plot()
mainFrame[roiY:roiY+roiH, roiX:roiX+roiW] = annotated_frame
cv2.rectangle(mainFrame, (roiX,roiY), (roiX+roiW,roiY+roiH), (128,0,128), 1)
cv2.imshow("YOLOv8 Inference", annotated_frame)
cv2.imshow("YOLOv8 Inference M", mainFrame)
if cv2.waitKey(1) & 0xFF == ord("q"):
break
else:
break
cap.release()
cv2.destroyAllWindows()

