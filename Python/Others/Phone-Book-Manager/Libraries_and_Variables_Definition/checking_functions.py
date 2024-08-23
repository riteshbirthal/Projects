from Libraries_and_Variables_Definition.libraries_and_variables import *


def check_id(id_):
    id_ = id_.strip()
    if len(id_) and id_.isdigit() and (int(id_) < len(contact_database)):
        return True
    return False


def name_valid(f_name, m_name, l_name):
    check = [1, 1, 1, 1]
    if len(f_name.strip()) == 0 and f_name.strip().isalpha():
        check[0] = 0
    if len(m_name.strip()) == 0 and m_name.strip().isalpha():
        check[1] = 0
    if len(l_name.strip()) == 0 and l_name.strip().isalpha():
        check[2] = 0
    if check[0] + check[1] + check[2] == 0:
        check[3] = 0
    return check


def email_valid(email):
    email = email.strip()
    check = [0, 0, 0]
    if not (email[0].isdigit() or email[0].isalpha()):
        return 0
    for i in range(len(email)):
        if email[i] == '@':
            check[0] = 1
        elif email[i] == '.':
            if check[0]:
                check[1], check[2] = 1, 1
            else:
                check[2] = 1
    if check[0] + check[1] + check[2] != 3:
        return 0
    return 1


def phone_valid(phone):
    phone = phone.strip()
    valid, exists = 0, 0
    if (not len(phone)) or (not phone.isdigit()):
        return [valid, exists]
    if phone in phone_numbers:
        exists = 1
    if len(phone) == 10:
        valid = 1
    return [valid, exists]


def submit(person):
    response = [1, 1, 1, 1, 1, 1]
    response[0], response[1], response[2], response[5] = \
        name_valid(person.first_name, person.middle_name, person.last_name)
    if email_valid(person.email) == 0:
        response[4], response[5] = 0, 0
    if phone_valid(person.phone)[0] == 0 or phone_valid(person.phone)[1]:
        response[4], response[5] = 0, 0
    return response


def add_person(person):
    if person.first_name in first_names.keys():
        first_names[person.first_name].append(person.id_)
    else:
        first_names[person.first_name] = [person.id_]
    if person.middle_name in middle_names.keys():
        middle_names[person.middle_name].append(person.id_)
    else:
        middle_names[person.middle_name] = [person.id_]
    if person.last_name in last_names.keys():
        last_names[person.last_name].append(person.id_)
    else:
        last_names[person.last_name] = [person.id_]
    if person.email in emails.keys():
        emails[person.email].append(person.id_)
    else:
        emails[person.email] = [person.id_]
    phone_numbers[person.phone] = person.id_


def predict_dict(text):
    if text == "First Name":
        return first_names
    elif text == "Middle Name":
        return middle_names
    elif text == "Last Name":
        return last_names
    elif text == "Email":
        return emails
    else:
        return {}


def predict_coord(text):
    if text == "First Name":
        return fn_disp_coord
    elif text == "Middle Name":
        return mn_disp_coord
    elif text == "Last Name":
        return ln_disp_coord
    elif text == "Email":
        return e_disp_coord
    elif text == "Phone":
        return p_disp_coord
    else:
        return id_disp_coord


def check_mouse_hover(bound, mouse):
    if bound[0][0] <= mouse[0] <= bound[0][1] and bound[1][0] <= mouse[1] <= bound[1][1]:
        return True
    return False


def get_bound(screen, x1, x2, y1, y2):
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    return [[screen_width * x1, screen_width * x2], [screen_height * y1, screen_height * y2]]


def get_coord(screen, x, y):
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    return screen_width * x, screen_height * y


def get_button(text, font):
    normal = font.render(text, True, white)
    pressed = font.render(text, True, white_)
    return normal, pressed


def get_rect_coord(screen, x1, y1, x2, y2):
    screen_width, screen_height = screen.get_width(), screen.get_height()
    return screen_width * x1, screen_height * y1, screen_width * x2, screen_height * y2
