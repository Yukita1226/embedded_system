import cv2
from ultralytics import YOLO

model = YOLO('/home/pi/OpenCV_File/data/yolov8n.pt', verbose=False)

path1 = "/home/pi/OpenCV_File/image/put something here.jpg"
path2 = "/home/pi/OpenCV_File/image/inot tell you lol.jpg"

results = model.predict(path1, conf=0.75)
annotated_frame = results[0].plot()
cv2.imshow("YOLOv8 Result", annotated_frame)
cv2.waitKey()
cv2.destroyAllWindows()
