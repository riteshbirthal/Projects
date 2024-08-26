import cv2
import numpy as np
import pytesseract

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    a, b = gray.shape

    for i in range(a):
        for j in range(b):
            if gray[i, j] < 125:
                gray[i, j] = 0
            else:
                gray[i, j] = 255
    
    # Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Adaptive Thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    # Morphological operations (optional, tweak kernel size)
    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    return morph

def extract_digit(cell):
    # Resize the image to a fixed size (for consistency)
    cell_resized = cv2.resize(cell, (50, 50))
    
    # Add padding around the digit
    padded = cv2.copyMakeBorder(cell_resized, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    
    # Invert colors (for better contrast)
    padded_inverted = cv2.bitwise_not(padded)
    
    return padded_inverted

def recognize_digit(image):
    config = '--psm 10 --oem 1 -c tessedit_char_whitelist=0123456789'
    digit = pytesseract.image_to_string(image, config=config)
    return digit.strip()

# Load and preprocess the Sudoku image
image = cv2.imread('sudoku2.jpeg')
processed_image = preprocess_image(image)

cv2.imshow('processed image', processed_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

# Assume `warped` is the perspective-transformed Sudoku grid image (as in the previous code)
cell_size = processed_image.shape[0] // 9
grid = np.zeros((9, 9), dtype=int)

for i in range(9):
    for j in range(9):
        cell = processed_image[i*cell_size:(i+1)*cell_size, j*cell_size:(j+1)*cell_size]
        digit_image = extract_digit(cell)
        
        digit = recognize_digit(digit_image)
        if digit.isdigit():
            grid[i, j] = int(digit)

print(grid)
