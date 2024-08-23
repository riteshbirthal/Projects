from Libraries_and_Variables_Definition.checking_functions import *


def display_names(screen, contact_id=0):
    person = Contact()
    running = True
    rectangle_color = [0, 0, 0]
    while running:
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        screen.fill(background_colour)
        x, y, w, h = get_rect_coord(screen, 0.28, 0.1, 0.4, 0.1)
        h_ = screen_height * 0.135
        first_name_rect = pygame.Rect(x, y + h_, w, h)
        middle_name_rect = pygame.Rect(x, y + 2 * h_, w, h)
        last_name_rect = pygame.Rect(x, y + 3 * h_, w, h)
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        submit_text, submit_text_pressed = get_button('Submit', font)
        exit_text, exit_text_pressed = get_button('Back to Main Menu', font)
        mouse = pygame.mouse.get_pos()
        # Submit button
        submit_bound = get_bound(screen, 0.4, 0.53, 0.64, 0.7)
        submit_coord = get_coord(screen, 0.4, 0.62)
        if check_mouse_hover(submit_bound, mouse):
            screen.blit(submit_text_pressed, submit_coord)

        else:
            screen.blit(submit_text, submit_coord)
        # back to menu button
        ex_bound = get_bound(screen, 0.30, 0.65, 0.74, 0.8)
        ex_coord = get_coord(screen, 0.30, 0.72)
        if check_mouse_hover(ex_bound, mouse):
            screen.blit(exit_text_pressed, ex_coord)
        else:
            screen.blit(exit_text, ex_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return [person, 2, contact_id]
            if event.type == pygame.MOUSEBUTTONDOWN:
                # submit button
                if check_mouse_hover(submit_bound, mouse):
                    return [person, 0, contact_id]
                # back to main menu button
                if check_mouse_hover(ex_bound, mouse):
                    return [person, 1, contact_id]
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
            if event.type == pygame.KEYDOWN and rectangle_color[2]:
                if event.key == pygame.K_BACKSPACE:
                    person.last_name = person.last_name[:-1]
                elif event.key == pygame.K_RETURN:
                    return [person, 0, contact_id]
                else:
                    person.last_name += event.unicode
            if event.type == pygame.KEYDOWN and rectangle_color[1]:
                if event.key == pygame.K_BACKSPACE:
                    person.middle_name = person.middle_name[:-1]
                elif event.key == pygame.K_RETURN:
                    rectangle_color[1], rectangle_color[2] = 0, 1
                else:
                    person.middle_name += event.unicode
            if event.type == pygame.KEYDOWN and rectangle_color[0]:
                if event.key == pygame.K_BACKSPACE:
                    person.first_name = person.first_name[:-1]
                elif event.key == pygame.K_RETURN:
                    rectangle_color[0], rectangle_color[1] = 0, 1
                else:
                    person.first_name += event.unicode
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

        if len(person.first_name):
            first_name_surface = font.render(person.first_name, True, (0, 0, 0))
        else:
            first_name_surface = font.render('First Name', True, (150, 150, 150))
        if len(person.middle_name):
            middle_name_surface = font.render(person.middle_name, True, (0, 0, 0))
        else:
            middle_name_surface = font.render('Middle Name', True, (150, 150, 150))
        if len(person.last_name):
            last_name_surface = font.render(person.last_name, True, (0, 0, 0))
        else:
            last_name_surface = font.render('Last Name', True, (150, 150, 150))
        screen.blit(first_name_surface, (first_name_rect.x + screen_width * 0.1,
                                         first_name_rect.y + screen_height * 0.004))
        first_name_rect.w = max(100, first_name_surface.get_width() + 10)

        screen.blit(middle_name_surface, (middle_name_rect.x + screen_width * 0.08,
                                          middle_name_rect.y + screen_height * 0.004))
        middle_name_rect.w = max(100, middle_name_surface.get_width() + 10)

        screen.blit(last_name_surface, (last_name_rect.x + screen_width * 0.1,
                                        last_name_rect.y + screen_height * 0.004))
        last_name_rect.w = max(100, last_name_surface.get_width() + 10)
        pygame.display.update()
