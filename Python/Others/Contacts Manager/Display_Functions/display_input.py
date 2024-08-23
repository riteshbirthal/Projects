from Libraries_and_Variables_Definition.checking_functions import *


def display_email(screen, id_):
    return display_input("Email", screen, 0.28, 0.4, 0.4, 0.1, 0.13, 0.005, id_)


def display_id(screen):
    return display_input("ID", screen, 0.28, 0.4, 0.4, 0.1, 0.18, 0.005)


def display_phone(screen):
    return display_input("Phone", screen, 0.28, 0.4, 0.4, 0.1, 0.13, 0.005)


def display_phone_id(screen, id_):
    return display_input("Phone", screen, 0.28, 0.4, 0.4, 0.1, 0.13, 0.005, id_)


def display_input(text, screen, x1, y1, x2, y2, x3, y3, contact_id=0):
    active = False
    running = True
    user_id = ""
    while running:
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        screen.fill(background_colour)
        x, y, w, h = get_rect_coord(screen, x1, y1, x2, y2)
        user_id_rect = pygame.Rect(x, y, w, h)
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        submit_text, submit_text_pressed = get_button('Submit', font)
        exit_text, exit_text_pressed = get_button('Back to Main Menu', font)
        mouse = pygame.mouse.get_pos()
        # submit button
        submit_bound = get_bound(screen, 0.4, 0.60, 0.55, 0.61)
        submit_coord = get_coord(screen, 0.4, 0.53)
        if check_mouse_hover(submit_bound, mouse):
            screen.blit(submit_text_pressed, submit_coord)

        else:
            screen.blit(submit_text, submit_coord)
        # back to menu button
        back_to_menu_bound = get_bound(screen, 0.30, 0.65, 0.65, 0.71)
        back_to_menu_coord = get_coord(screen, 0.30, 0.63)
        if check_mouse_hover(back_to_menu_bound, mouse):
            screen.blit(exit_text_pressed, back_to_menu_coord)
        else:
            screen.blit(exit_text, back_to_menu_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return [user_id, 2, contact_id]
            if event.type == pygame.MOUSEBUTTONDOWN:
                # submit button
                if check_mouse_hover(submit_bound, mouse):
                    return [user_id, 0, contact_id]
                # back to main menu button
                if check_mouse_hover(back_to_menu_bound, mouse):
                    return [user_id, 1, contact_id]
                # input box
                if user_id_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    user_id = user_id[:-1]
                elif event.key == pygame.K_RETURN:
                    return [user_id, contact_id]
                else:
                    user_id += event.unicode
        if active:
            pygame.draw.rect(screen, white_, user_id_rect)
        else:
            pygame.draw.rect(screen, white, user_id_rect)

        if len(user_id):
            user_id_surface = font.render(user_id, True, (0, 0, 0))
            screen.blit(user_id_surface, (user_id_rect.x + screen_width * 0.02,
                                          user_id_rect.y + screen_height * 0.0025))
        else:
            user_id_surface = font.render(text, True, (150, 150, 150))
            screen.blit(user_id_surface, (user_id_rect.x + screen_width * x3, user_id_rect.y + screen_height * y3))
        user_id_rect.w = max(100, user_id_surface.get_width() + 10)
        pygame.display.update()
