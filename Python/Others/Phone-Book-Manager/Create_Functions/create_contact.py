from Create_Functions.create_contact_functions import *
from Display_Functions.display_input_names import *


def name_valid(f_name, m_name, l_name):
    check = [1, 1, 1, 1]
    if len(f_name.strip()) == 0:
        check[0] = 0
    if len(m_name.strip()) == 0:
        check[1] = 0
    if len(l_name.strip()) == 0:
        check[2] = 0
    if check[0] + check[1] + check[2] == 0:
        check[3] = 0
    return check


def email_valid(email):
    email = email.strip()
    check = [0, 0, 0]
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
    if phone in phone_numbers.keys():
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
    if not (phone_valid(person.phone)[0] == 1 and phone_valid(person.phone)[1] == 0):
        response[4], response[5] = 0, 0
    return response


def create_contact(screen):
    person = Contact()
    running = True
    rectangle_color = [0, 0, 0, 0, 0]
    while running:
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        screen.fill(background_colour)
        x, y, w, h = screen_width*0.28, screen_height*0.1, screen_width*0.4, screen_height*0.1
        h_ = screen_height*0.135
        first_name_rect = pygame.Rect(x, y, w, h)
        middle_name_rect = pygame.Rect(x, y + h_, w, h)
        last_name_rect = pygame.Rect(x, y + 2*h_, w, h)
        email_rect = pygame.Rect(x, y + 3*h_, w, h)
        phone_rect = pygame.Rect(x, y + 4*h_, w, h)
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        create_contact_text = font.render('Create Contact', True, white)
        create_contact_text_pressed = font.render('Create Contact', True, white_)
        exit_text = font.render('Back to Main Menu', True, white)
        exit_text_pressed = font.render('Back to Main Menu', True, white_)
        mouse = pygame.mouse.get_pos()
        # create contact button
        cc_bound = [[screen_width * 0.33, screen_width * 0.60], [screen_height * 0.77, screen_height * 0.83]]
        cc_coord = (screen_width * 0.33, screen_height * 0.75)
        if cc_bound[0][0] <= mouse[0] <= cc_bound[0][1] and cc_bound[1][0] <= mouse[1] <= cc_bound[1][1]:
            screen.blit(create_contact_text_pressed, cc_coord)

        else:
            screen.blit(create_contact_text, cc_coord)
        # back to menu button
        ex_bound = [[screen_width * 0.30, screen_width * 0.65], [screen_height * 0.87, screen_height * 0.93]]
        ex_coord = (screen_width * 0.30, screen_height * 0.85)
        if ex_bound[0][0] <= mouse[0] <= ex_bound[0][1] and ex_bound[1][0] <= mouse[1] <= ex_bound[1][1]:
            screen.blit(exit_text_pressed, ex_coord)
        else:
            screen.blit(exit_text, ex_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # create contact button
                if cc_bound[0][0] <= mouse[0] <= cc_bound[0][1] and cc_bound[1][0] <= mouse[1] <= cc_bound[1][1]:
                    if submit(person)[5]:
                        if save_contact(person, screen) is False:
                            return False
                        else:
                            person = Contact()
                    elif not name_valid(person.first_name, person.middle_name, person.last_name)[3]:
                        if not pyautogui.alert("Invalid Name!\n" + contact_invalid_text):
                            return False
                    elif not email_valid(person.email):
                        if not pyautogui.alert("Invalid Email!\n" + contact_invalid_text):
                            return False
                    elif phone_valid(person.phone)[1]:
                        if not pyautogui.alert("This phone number already exists."):
                            return False
                    else:
                        if not pyautogui.alert("Invalid Phone Number!\n" + contact_invalid_text):
                            return False
                # back to main menu button
                if ex_bound[0][0] <= mouse[0] <= ex_bound[0][1] and ex_bound[1][0] <= mouse[1] <= ex_bound[1][1]:
                    return True
                # input box
                if first_name_rect.collidepoint(event.pos):
                    rectangle_color[0] = 1
                else:
                    rectangle_color[0] = 0
                if middle_name_rect.collidepoint(event.pos):
                    rectangle_color[1] = 1
                else:
                    rectangle_color[1] = 0
                if last_name_rect.collidepoint(event.pos):
                    rectangle_color[2] = 1
                else:
                    rectangle_color[2] = 0
                if email_rect.collidepoint(event.pos):
                    rectangle_color[3] = 1
                else:
                    rectangle_color[3] = 0
                if phone_rect.collidepoint(event.pos):
                    rectangle_color[4] = 1
                else:
                    rectangle_color[4] = 0

            if event.type == pygame.KEYDOWN and rectangle_color[0]:
                if event.key == pygame.K_BACKSPACE:
                    person.first_name = person.first_name[:-1]
                elif event.key == pygame.K_RETURN:
                    rectangle_color[0], rectangle_color[1] = 0, 1
                else:
                    person.first_name += event.unicode
            if event.type == pygame.KEYDOWN and rectangle_color[1]:
                if event.key == pygame.K_BACKSPACE:
                    person.middle_name = person.middle_name[:-1]
                elif event.key == pygame.K_RETURN:
                    rectangle_color[1], rectangle_color[2] = 0, 1
                else:
                    person.middle_name += event.unicode
            if event.type == pygame.KEYDOWN and rectangle_color[2]:
                if event.key == pygame.K_BACKSPACE:
                    person.last_name = person.last_name[:-1]
                elif event.key == pygame.K_RETURN:
                    rectangle_color[2], rectangle_color[3] = 0, 1
                else:
                    person.last_name += event.unicode
            if event.type == pygame.KEYDOWN and rectangle_color[3]:
                if event.key == pygame.K_BACKSPACE:
                    person.email = person.email[:-1]
                elif event.key == pygame.K_RETURN:
                    rectangle_color[3], rectangle_color[4] = 0, 1
                else:
                    person.email += event.unicode
            if event.type == pygame.KEYDOWN and rectangle_color[4]:
                if event.key == pygame.K_BACKSPACE:
                    person.phone = person.phone[:-1]
                elif event.key == pygame.K_RETURN:
                    if submit(person)[5]:
                        if save_contact(person, screen) is False:
                            return False
                        else:
                            person = Contact()
                    elif not name_valid(person.first_name, person.middle_name, person.last_name)[3]:
                        if not pyautogui.alert("Invalid Name!\n" + contact_invalid_text):
                            return False
                    elif not email_valid(person.email):
                        if not pyautogui.alert("Invalid Email!\n" + contact_invalid_text):
                            return False
                    elif phone_valid(person.phone)[1]:
                        if not pyautogui.alert("This phone number already exists."):
                            return False
                    else:
                        if not pyautogui.alert("Invalid Phone Number!\n" + contact_invalid_text):
                            return False
                else:
                    person.phone += event.unicode
        if rectangle_color[0]:
            pygame.draw.rect(screen, white_, first_name_rect)
        else:
            pygame.draw.rect(screen, white, first_name_rect)
        if rectangle_color[1]:
            pygame.draw.rect(screen, white_, middle_name_rect)
        else:
            pygame.draw.rect(screen, white, middle_name_rect)
        if rectangle_color[2]:
            pygame.draw.rect(screen, white_, last_name_rect)
        else:
            pygame.draw.rect(screen, white, last_name_rect)
        if rectangle_color[3]:
            pygame.draw.rect(screen, white_, email_rect)
        else:
            pygame.draw.rect(screen, white, email_rect)
        if rectangle_color[4]:
            pygame.draw.rect(screen, white_, phone_rect)
        else:
            pygame.draw.rect(screen, white, phone_rect)

        if len(person.first_name):
            first_name_surface = font.render(person.first_name, True, (0, 0, 0))
            screen.blit(first_name_surface, (first_name_rect.x + screen_width * 0.002,
                                             first_name_rect.y + screen_height * 0.004))
        else:
            first_name_surface = font.render('First Name', True, (150, 150, 150))
            screen.blit(first_name_surface, (first_name_rect.x + screen_width * 0.1,
                                             first_name_rect.y + screen_height * 0.004))
        if len(person.middle_name):
            middle_name_surface = font.render(person.middle_name, True, (0, 0, 0))
            screen.blit(middle_name_surface, (middle_name_rect.x + screen_width * 0.002,
                                              middle_name_rect.y + screen_height * 0.004))
        else:
            middle_name_surface = font.render('Middle Name', True, (150, 150, 150))
            screen.blit(middle_name_surface, (middle_name_rect.x + screen_width * 0.08,
                                              middle_name_rect.y + screen_height * 0.004))
        if len(person.last_name):
            last_name_surface = font.render(person.last_name, True, (0, 0, 0))
            screen.blit(last_name_surface, (last_name_rect.x + screen_width * 0.002,
                                            last_name_rect.y + screen_height * 0.004))
        else:
            last_name_surface = font.render('Last Name', True, (150, 150, 150))
            screen.blit(last_name_surface, (last_name_rect.x + screen_width * 0.1,
                                            last_name_rect.y + screen_height * 0.004))
        if len(person.email):
            email_surface = font.render(person.email, True, (0, 0, 0))
            screen.blit(email_surface, (email_rect.x + screen_width * 0.002, email_rect.y + screen_height * 0.004))
        else:
            email_surface = font.render('Email', True, (150, 150, 150))
            screen.blit(email_surface, (email_rect.x + screen_width * 0.13, email_rect.y + screen_height * 0.004))
        if len(person.phone):
            phone_surface = font.render(person.phone, True, (0, 0, 0))
            screen.blit(phone_surface, (phone_rect.x + screen_width * 0.002, phone_rect.y + screen_height * 0.004))
        else:
            phone_surface = font.render('Phone', True, (150, 150, 150))
            screen.blit(phone_surface, (phone_rect.x + screen_width * 0.13, phone_rect.y + screen_height * 0.004))

        first_name_rect.w = max(100, first_name_surface.get_width() + 10)

        middle_name_rect.w = max(100, middle_name_surface.get_width() + 10)

        last_name_rect.w = max(100, last_name_surface.get_width() + 10)

        email_rect.w = max(100, email_surface.get_width() + 10)

        phone_rect.w = max(100, phone_surface.get_width() + 10)
        pygame.display.update()
