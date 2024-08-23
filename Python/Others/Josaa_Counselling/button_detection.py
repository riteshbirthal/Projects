import cv2
import pyautogui
import numpy as np

def detect_button_on_screen(image_path, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    button_template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    result = cv2.matchTemplate(screenshot, button_template, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= threshold:
        buttton_x, button_y = max_loc
        button_w, button_h = button_template.shape[1], button_template.shape[0]
        return True, (buttton_x, button_y, button_w, button_h)
    else:
        return False, None
    
def clicking_button(image_path, threshold=0.8):
    is_button, button_location = detect_button_on_screen(image_path, threshold)

    if is_button:
        print("button present...: ", button_location)
        pyautogui.click(x=(button_location[0] + button_location[2]/2), y=(button_location[1] + button_location[3]/2))
        return True
    else:
        print("button not detected..")
        return False