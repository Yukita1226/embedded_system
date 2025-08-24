import cv2
path = '/home/pi/OpenCV_File/video/Car_FangMaster.mp4'
cap = cv2.VideoCapture(path)
while cap.isOpened():
ret, frame = cap.read()
if not ret:
  break

cv2.imshow('Frame', frame)

if cv2.waitKey(1) & 0xFF == ord('q'):
  break

cap.release()
# Destroys all windows
cv2.destroyAllWindows()
