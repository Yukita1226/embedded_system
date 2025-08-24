# 10-with Tracker
import cv2
cap = cv2.VideoCapture('/home/pi/OpenCV_File/video/ThaiTraffic04_480.mp4')
roiX,roiY,roiW,roiH = 10, 50, 350, 400

from M60_tracker import *
tracker = EuclideanDistTracker()
object_detector = cv2.createBackgroundSubtractorMOG2()
font = cv2.FONT_HERSHEY_PLAIN
nCar = 0

while(cap.isOpened()):
  ret, frame = cap.read()
  if frame is None:
  break
  result = frame.copy()
  mask = object_detector.apply(frame)
  contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  detections = []
  for cnt in contours:

    area = cv2.contourArea(cnt)
    if area > 4000:
      cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 1)
      x, y, w, h = cv2.boundingRect(cnt)
      detections.append([x, y, w, h])
      boxes_ids = tracker.update(detections)
  for box_id in boxes_ids:
    x, y, w, h, id = box_id
    nCar = id
    cv2.putText(result, str(id), (x, y - 15), font, 2, (255, 0, 0), 2)
    cv2.rectangle(result, (x, y), (x+w, y+h), (255, 0, 0), 1)
  cv2.rectangle(result, (roiX, roiY), (roiX+roiW, roiY+roiH), (125, 0, 125), 1)
  cv2.putText(result, "nCar = " + str(nCar), (roiX+roiW, roiY+roiH), font, 2, (255, 0, 0), 2)
  cv2.imshow("Mask", mask)
  cv2.imshow("Frame", frame)
  cv2.imshow("Result", result)
  if cv2.waitKey(1) & 0xFF == ord("q"):
  break
cap.release()
cv2.destroyAllWindows()
