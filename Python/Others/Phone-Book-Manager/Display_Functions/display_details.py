from Libraries_and_Variables_Definition.checking_functions import *


def display_details(screen, id_, prev_=1, next_=1):  # prev and next shows button visibility
    person = contact_database[id_]
    running = True
    while running:
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width * 0.04))
        font_button = pygame.font.SysFont('arial', int(screen_width * 0.05))
        x, y, w, h = get_rect_coord(screen, 0.65, 0.1, 0.28, 0.5)
        photo_rect = pygame.Rect(x, y, w, h)
        pre_button_text, pre_button_text_pressed = get_button('prev', font_button)
        next_button_text, next_button_text_pressed = get_button('next', font_button)
        if prev_ or next_:
            prev_next_height = 0.1
        else:
            prev_next_height = 0
        pygame.draw.rect(screen, white, photo_rect)
        if x == 0:
            photo_surface = font.render('Loading..', True, (0, 0, 0))
            screen.blit(photo_surface, (photo_rect.x + screen_width * 0.05, photo_rect.y + screen_height * 0.2))
        else:
            photo_surface = font.render('PHOTO', True, (150, 150, 150))
            screen.blit(photo_surface, (photo_rect.x + screen_width * 0.08, photo_rect.y + screen_height * 0.2))
        # pygame.draw.rect(screen, white, photo_rect)
        id_text = font.render('ID: ' + str(person.id_), True, white)
        phone_text = font.render('PHONE: ' + person.phone, True, white)
        name_text = font.render('NAME: ' + person.first_name.upper() + " " + person.middle_name.upper() +
                                " " + person.last_name.upper(), True, white)
        email_text = font.render('EMAIL: ' + person.email.upper(), True, white)
        exit_text, exit_text_pressed = get_button('Back to Main Menu', font_button)
        mouse = pygame.mouse.get_pos()
        # id
        id_coord = get_coord(screen, 0.12, 0.25)
        screen.blit(id_text, id_coord)
        # phone
        phone_coord = get_coord(screen, 0.12, 0.33)
        screen.blit(phone_text, phone_coord)
        # name
        name_coord = get_coord(screen, 0.12, 0.41)
        screen.blit(name_text, name_coord)
        # email
        email_coord = get_coord(screen, 0.12, 0.49)
        screen.blit(email_text, email_coord)
        # previous button
        previous_bound = get_bound(screen, 0.31, 0.39, 0.67, 0.73)
        previous_coord = get_coord(screen, 0.31, 0.65)
        # next button
        next_bound = get_bound(screen, 0.53, 0.61, 0.67, 0.73)
        next_coord = get_coord(screen, 0.53, 0.65)
        if prev_ or next_:
            if check_mouse_hover(previous_bound, mouse) or prev_ == 0:
                screen.blit(pre_button_text_pressed, previous_coord)
            elif prev_ or next_:
                screen.blit(pre_button_text, previous_coord)
            if check_mouse_hover(next_bound, mouse) or next_ == 0:
                screen.blit(next_button_text_pressed, next_coord)
            elif prev_ or next_:
                screen.blit(next_button_text, next_coord)
        # exit button
        exit_bound = get_bound(screen, 0.28, 0.62, 0.67 + prev_next_height, 0.73 + prev_next_height)
        exit_coord = get_coord(screen, 0.28, 0.65 + prev_next_height)
        if check_mouse_hover(exit_bound, mouse):
            screen.blit(exit_text_pressed, exit_coord)
        else:
            screen.blit(exit_text, exit_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return [0, 0, 2]
            if event.type == pygame.MOUSEBUTTONDOWN:
                # previous button
                if check_mouse_hover(previous_bound, mouse) and prev_:
                    return [1, 0, 0]
                # next button
                if check_mouse_hover(next_bound, mouse) and next_:
                    return [0, 1, 0]
                # back to main menu button
                if check_mouse_hover(exit_bound, mouse):
                    return [0, 0, 1]
        pygame.display.update()
