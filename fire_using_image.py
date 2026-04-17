import cv2
from ultralytics import YOLO

model = YOLO(r"D:\python\projects\fire_detection\runs\detect\train\weights\best.pt")
img = cv2.imread(r"D:\python\projects\fire_detection\Dataset\train\images\50 - Copy.jpg")
result = model.predict(img)

#image with bounding boxes 
im = result[0].plot() 
cv2.imshow("fire", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
