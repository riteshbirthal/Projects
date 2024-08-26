import numpy as np
import cv2
# from tensorflow.keras.models import load_model
import pytesseract


# def initializePredectionModel(model_path):
#     model = load_model(model_path)
#     return model

def preProcess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 1)
    thresholdImage = cv2.adaptiveThreshold(blurred, 255, 1, 1, 11, 2)
    return thresholdImage

def displayImage(img, s):
    cv2.imshow('Current State: ', img)
    cv2.waitKey(s * 1000)
    cv2.destroyAllWindows()

def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area

def reorder(points):
    points = points.reshape((4, 2))
    newPoints = np.zeros((4, 1, 2), dtype=np.int32)
    add = points.sum(1)
    newPoints[0] = points[np.argmin(add)]
    newPoints[3] = points[np.argmax(add)]
    diff = np.diff(points, axis=1)
    newPoints[1] = points[np.argmin(diff)]
    newPoints[2] = points[np.argmax(diff)]
    return newPoints

def gray_scale_image(image, flag):
    if flag:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    a, b = gray.shape
    for i in range(a):
        for j in range(b):
            if gray[i, j] < 150:
                gray[i, j] = 0
            else:
                gray[i, j] = 255
    return gray

def extract_digit(cell):
    cell_resized = cv2.resize(cell, (50, 50))
    # cell_resized = gray_scale_image(cell_resized, True)
    padded = cv2.copyMakeBorder(cell_resized, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    padded_inverted = cv2.bitwise_not(padded)
    return padded_inverted
    # return padded

def recognize_digit(image):
    config = '--psm 6'
    # config = '--psm 10 --oem 1 -c tessedit_char_whitelist=123456789'
    digit = pytesseract.image_to_string(image, config=config)
    return digit.strip()

imagePath = "sudoku2.jpeg"
imageHeight = 450
imageWidth = 450


img = cv2.imread(imagePath)
img = cv2.resize(img, (imageWidth, imageHeight))
imgBlank = np.zeros((imageHeight, imageWidth, 3), np.uint8)
thresholdImage = preProcess(img)

# displayImage(img, 10)

# displayImage(thresholdImage, 10)

contoursImage = img.copy()
bigCountourImage = img.copy()
contours, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(contoursImage, contours, -1, (0, 255, 0), 3)

# displayImage(contoursImage, 10)

biggest, maxArea = biggestContour(contours)
if biggest.size != 0:
    biggest = reorder(biggest)
    cv2.drawContours(bigCountourImage, biggest, -1, (255, 0, 0), 10)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [imageWidth, 0], [0, imageHeight], [imageWidth, imageHeight]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    warpColoredImage = cv2.warpPerspective(img, matrix, (imageWidth, imageHeight))
    detectedDigitsImage = imgBlank.copy()
    warpColoredImage = gray_scale_image(warpColoredImage, True)
    displayImage(warpColoredImage, 10)

    cell_size = warpColoredImage.shape[0] // 9
    grid = np.zeros((9, 9), dtype=int)

    for i in range(9):
        for j in range(9):
            cell = warpColoredImage[i*cell_size:(i+1)*cell_size, j*cell_size:(j+1)*cell_size]
            digit_image = extract_digit(cell)
            # displayImage(digit_image, 2)
            
            digit = recognize_digit(digit_image)
            if digit.isdigit():
                grid[i, j] = int(digit)

    print(grid)



