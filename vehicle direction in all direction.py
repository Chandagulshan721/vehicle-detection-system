import cv2
import imutils
cascade_src = 'cars.xml' 
car_cascade=cv2.CascadeClassifier(cascade_src)

cam=cv2.VideoCapture(0)

while True:
     _,img= cam.read()

     img=imutils.resize(img,width=800)

     gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

     cars=car_cascade.detectMultiScale(gray,1.1,1)

     for (x,y,w,h) in cars:
         cv2.rectangle(img,(x, y),(x + w,y + h),(0 ,0 , 255), 2)

     cv2.imshow("Frame",img)

     b=(len(cars))
     print("_______________________")
     print(f"North:{b}")
     if b>=8:
         print("North More Traffic,please on the RED signal")
     elif b<=8:
         print("South More Traffic,Please on the RED sihgnal")
     else:    
         print("no traffic")
         
     if cv2.waitKey(33)==27:
         break
cam.release()
cv2.destroyAllWindows()
