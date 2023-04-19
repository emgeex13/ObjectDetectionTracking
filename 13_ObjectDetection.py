import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0 , 255, nothing) #lower hue
cv2.createTrackbar("LS", "Tracking", 0 , 255, nothing) #lower saturation
cv2.createTrackbar("LV", "Tracking", 0 , 255, nothing) #lower value
cv2.createTrackbar("UH", "Tracking", 255 , 255, nothing)#Upper hue
cv2.createTrackbar("US", "Tracking", 255 , 255, nothing)#Upper saturation
cv2.createTrackbar("UV", "Tracking", 255 , 255, nothing)#Upper value
while(True):
    frame = cv2.imread("smarties.png")
    # frame = cv2.imread("hidden_160.jpg")
    # ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("LH","Tracking" )
    l_s = cv2.getTrackbarPos("LS","Tracking" )
    l_v = cv2.getTrackbarPos("LV","Tracking" )
    u_h = cv2.getTrackbarPos("UH","Tracking" )
    u_s = cv2.getTrackbarPos("US","Tracking" )
    u_v = cv2.getTrackbarPos("UV","Tracking" )

    l_b = np.array([l_h,l_s,l_v])  #lower bound
    u_b = np.array([u_h,u_s,u_v]) #upper bound

    # Creating a mask
    mask = cv2.inRange(hsv, l_b, u_b) 

    # bitwise and with mask
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("hsv", hsv)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key ==27:
        break

cv2.release()
cv2.destroyAllWindows()