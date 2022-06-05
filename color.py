import fractions
from pickle import REDUCE
import cv2
import pandas as pd

cap = cv2.VideoCapture(0)


#READING THE CSV FILE
index = ["color", "Name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# TO GET THE COLOR OF THE OBJECT FOCUSSED
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            color = csv.loc[i, "Name"]
    return color

def video_capture():

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)  


while True:

    _, frame = cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height,width, _ = frame.shape

    cx=int(width / 2)
    cy=int(height / 2)


    pixel_center = frame[cy,cx]
    hue_value=pixel_center[0]

    pixel_center_bgr = frame[cy,cx]
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])

    color =get_color_name(r,g,b)

    
    cv2.putText(frame,color,(10,50),0,2,(0,0,0),6)
    cv2.putText(frame,color,(10,50),0,2,(b,g,r),3)
    cv2.circle(frame,(cx,cy), 3 ,(0,255,0),2)

    cv2.imshow("Frame", frame)

    #WAITKEY = ENTER
    key=cv2.waitKey(1)
    if key==13:
        break


cap.release()
cv2.destroyAllWindows