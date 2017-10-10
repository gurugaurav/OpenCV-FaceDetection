import cv2

face_cascade = cv2.CascadeClassifier('/home/guru/Downloads/opencv/sources/data/haarcascades_cuda/haarcascade_frontalface_default.xml')

img = cv2.imread('home/guru/Downloads/faces.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces: 
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
roi_gray = gray[y:y+h, x:x+w] 
roi_color = img[y:y+h, x:x+w]

cv2.namedWindow('image',cv2.WINDOW_NORMAL) 
cv2.resizeWindow('image', 700,500) 
cv2.imshow('image',img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
