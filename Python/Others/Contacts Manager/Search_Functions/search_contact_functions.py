from Display_Functions.display_details import *
from Display_Functions.text_page import *
from Display_Functions.display_input import *
from Display_Functions.display_input_names import *


def ids_list(sub_str, text):
    id_list = []
    if text == "Phone":
        for phone in phone_numbers:
            if sub_str in phone:
                id_list.append(phone_numbers[phone])
    else:
        dict_ = predict_dict(text)
        for name in dict_:
            if sub_str in name:
                id_list = id_list + dict_[name]
        id_list = [*set(id_list)]
    return id_list


def display_ids(ids_, screen):
    i = 0
    while (i < len(ids_)) and (i >= 0):
        if i == 0:
            details_response = display_details(screen, ids_[i], 0, 1)
        elif i == len(ids_) - 1:
            details_response = display_details(screen, ids_[i], 1, 0)
        else:
            details_response = display_details(screen, ids_[i], 1, 1)
        if details_response[2] == 0:
            if details_response[0]:
                i -= 1
            else:
                i += 1
        elif details_response[2] == 2:
            return False
        else:
            break


def search_fun(text, screen):
    coord = predict_coord(text)
    while True:
        response = display_input(text, screen, coord[0], coord[1], coord[2], coord[3], coord[4], coord[5])
        if response[1] == 0:
            if len(response[0].strip()):
                ids_ = ids_list(response[0].strip().lower(), text)
                if len(ids_) == 0:
                    if no_record_found(screen) is False:
                        return False
                else:
                    if display_ids(ids_, screen) is False:
                        return False
            else:
                if no_record_found(screen) is False:
                    return False
        elif response[1] == 2:
            return False
        else:
            break
