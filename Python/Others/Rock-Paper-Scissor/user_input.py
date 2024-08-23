import cv2
import time
import pygame
import mediapipe as mp
from posture_detection import *

# initialize pygame
pygame.init()

# webcam video
cap = cv2.VideoCapture(0)
width = 640
height = 480
# width of window
cap.set(3, width)
# height of window
cap.set(4, height)
# brightness
cap.set(10, 100)
# white color
white = (255, 255, 255)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, model_complexity=1,
                      min_detection_confidence=0.90, min_tracking_confidence=0.90)


def user_gesture_input(screen, background_colour):
    user_gesture = ""
    time_init = time.time()
    t = time.time() - time_init
    while t <= 3:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width * 0.2))

        font_coord = (screen_width * 0.27, screen_height * 0.3)
        if (t >= 0) and (t < 1):
            screen.blit(font.render('Rock', True, white), font_coord)
        elif (t >= 1) and (t < 2):
            screen.blit(font.render('Paper', True, white), font_coord)
        elif t >= 2:
            screen.blit(font.render('Scissor', True, white), font_coord)

        # print(results)
        hand_det = results.multi_hand_landmarks
        if hand_det:
            hand = hand_det[0]
            posture = [[0, 0 * i] for i in range(21)]
            count = 0
            for f_id, l_mark in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(l_mark.x * w), int(l_mark.y * h)
                posture[count] = [cx, cy]
                count += 1
            user_gesture = find_gesture(posture)
            # mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
            # cv2.putText(img, gesture, (250, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
            # print(gesture)
        # cv2.imshow("Video", img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        t = time.time() - time_init
        pygame.display.update()
    return user_gesture