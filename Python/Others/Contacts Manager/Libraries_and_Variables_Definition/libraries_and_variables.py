import os
import pygame
import pickle
import pyautogui

pygame.init()

first_names = {}
middle_names = {}
last_names = {}
emails = {}
phone_numbers = {}
contact_database = []
path = 'contact_database/'

# white color
white = (255, 255, 255)
white_ = (100, 150, 200)

background_colour = (20, 100, 200)

fn_disp_coord = [0.28, 0.4, 0.4, 0.1, 0.1, 0.005]
mn_disp_coord = [0.28, 0.4, 0.4, 0.1, 0.08, 0.005]
ln_disp_coord = [0.28, 0.4, 0.4, 0.1, 0.1, 0.005]
e_disp_coord = [0.28, 0.4, 0.4, 0.1, 0.13, 0.005]
p_disp_coord = [0.28, 0.4, 0.4, 0.1, 0.13, 0.005]
id_disp_coord = [0.28, 0.4, 0.4, 0.1, 0.18, 0.005]

text1 = "Name contains Aphabates only.\n"
text2 = "Email must start with Alphanumeric key.\n"
text3 = "Phone number must be 10 digits.\n"
contact_invalid_text = text1 + text2 + text3


class Contact:
    id_, first_name, middle_name, last_name, email, phone = 0, "", "", "", "", ""
