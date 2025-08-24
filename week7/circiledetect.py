image_path = '/home/pi/OpenCV_File/image/can.jpg'
import cv2
import numpy as np
Cimg = cv2.imread(image_path)
Gimg = cv2.imread(image_path,0)
cv2.imshow ('Original Image', Cimg)
Gimg = cv2.medianBlur(Gimg,5)
circles = cv2. HoughCircles(Gimg,cv2.HOUGH_GRADIENT,1,100, param1=100, param2=30, minRadius=0, maxRadius=0)
if circles is not None:
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
cv2.circle(Cimg, (i[0],i[1]),i[2],(0,255,0),2)
cv2.circle(Cimg, (i[0],i[1]),2 ,(0,0,255),3)
else:
print('circle not found')
cv2.imshow ('Detected circles',Cimg)
cv2.waitKey (0)
cv2.destroyAllWindows()
