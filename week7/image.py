import cv2
image_path = '/home/pi/OpenCV_File/image/lena30.jpg'
img = cv2.imread(image_path)
cv2.imshow("Lena Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
