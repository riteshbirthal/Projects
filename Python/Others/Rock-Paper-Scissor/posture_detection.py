import numpy as np


def predict_result(gesture, comp_gesture):
    if gesture == "Rock" and comp_gesture == "Paper":
        return 'You Lose!'
    elif gesture == "Scissor" and comp_gesture == "Rock":
        return 'You Lose!'
    elif gesture == "Paper" and comp_gesture == "Scissor":
        return 'You Lose!'
    elif gesture == "Paper" and comp_gesture == "Rock":
        return 'You Won!'
    elif gesture == "Rock" and comp_gesture == "Scissor":
        return 'You Won!'
    elif gesture == "Scissor" and comp_gesture == "Paper":
        return 'You Won!'
    else:
        return 'Game Tie!'


def distance(point1, point2):
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def find_finger_gesture(dist, a, b, c, d):
    # return 1 if finger is open else return 0
    if dist[a] + dist[b] > d and dist[b] + dist[c] > d:
        return 0
    return 1


def find_gesture(posture):
    dist = []
    for i in range(20):
        dist.append(distance(posture[i], posture[i+1]))
    dist_ind = distance(posture[5], posture[8])
    dist_midd = distance(posture[9], posture[12])
    dist_ring = distance(posture[13], posture[16])
    dist_lit = distance(posture[17], posture[20])
    middle = find_finger_gesture(dist, 9, 10, 11, dist_midd)
    index = find_finger_gesture(dist, 5, 6, 7, dist_ind)
    ring = find_finger_gesture(dist, 13, 14, 15, dist_ring)
    little = find_finger_gesture(dist, 17, 18, 19, dist_lit)
    if index and middle and ring and little:
        gesture = "Paper"
    elif index and middle:
        gesture = "Scissor"
    else:
        gesture = "Rock"
    return gesture