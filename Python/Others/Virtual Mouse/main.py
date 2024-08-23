import cv2
import mediapipe as mp
import time
import pyautogui
import math

############################
wCam, hCam = 1280, 720
############################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
    )
mpDraw = mp.solutions.drawing_utils
k = 0
cx1, cy1 = 0, 0
l, m = [0,0], [0,0]
cx8,cx12,cy8,cy12 = 0,0,0,0
X, Y = pyautogui.size()
pyautogui.FAILSAFE = False
while True:
    k=k+1
    ret, img = cap.read()
    #imgRGB = cv2.flip(imgRGB,1)
    img2 = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(img.shape)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img2.shape
                mx, my = pyautogui.position()
                cx, cy = int(lm.x*w), int(lm.y*h)
                cv2.circle(img2,(cx,cy),5,(255,10,250),cv2.FILLED)
                if id ==8:
                    i = 3
                    mx = mx + i*(cx - cx1)
                    my = my + i*(cy - cy1)
                    if mx>X:
                        mx = X
                    elif my > Y:
                        my = Y
                    elif mx < 0:
                        mx = 0
                    elif my < 0:
                        my = 0
                    pyautogui.moveTo(mx,my)
                    cx1, cy1 = cx, cy
                #print(id,cx,cy)
                if id == 8 :
                    cx8, cy8 = cx, cy
                    l = [cx8,cy8]
                if id == 12 :
                    cx12, cy12 = cx, cy
                    m = [cx12,cy12]
                if math.dist(l,m)<10:
                    pyautogui.click()
                    #time.sleep(1)
                #print(math.dist(l,m))
            mpDraw.draw_landmarks(img2, handLms, mpHands.HAND_CONNECTIONS)
            
    #img = cv2.flip(img,1)
    cv2.imshow("Image", img2)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break