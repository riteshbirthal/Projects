from Libraries_and_Variables_Definition.checking_functions import *


def search_name(screen):
    running = True
    while running:
        screen.fill(background_colour)
        screen_width = screen.get_width()
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        search_font = pygame.font.SysFont('arial', int(screen_width * 0.08))
        search_text = search_font.render('Search By', True, white)
        first_name_text, first_name_text_pressed = get_button('First Name', font)
        middle_name_text, middle_name_text_pressed = get_button('Middle Name', font)
        last_name_text, last_name_text_pressed = get_button('Last Name', font)
        exit_text, exit_text_pressed = get_button('Back to Previous Menu', font)
        mouse = pygame.mouse.get_pos()
        sc_coord = get_coord(screen, 0.30, 0.18)
        screen.blit(search_text, sc_coord)
        # First Name button
        first_name_bound = get_bound(screen, 0.33, 0.54, 0.37, 0.43)
        first_name_coord = get_coord(screen, 0.33, 0.35)
        if check_mouse_hover(first_name_bound, mouse):
            screen.blit(first_name_text_pressed, first_name_coord)
        else:
            screen.blit(first_name_text, first_name_coord)
        #  Middle Name button
        middle_name_bound = get_bound(screen, 0.31, 0.56, 0.47, 0.53)
        middle_name_coord = get_coord(screen, 0.31, 0.45)
        if check_mouse_hover(middle_name_bound, mouse):
            screen.blit(middle_name_text_pressed, middle_name_coord)
        else:
            screen.blit(middle_name_text, middle_name_coord)
        # Last Name button
        last_name_bound = get_bound(screen, 0.33, 0.54, 0.57, 0.63)
        last_name_coord = get_coord(screen, 0.33, 0.55)
        if check_mouse_hover(last_name_bound, mouse):
            screen.blit(last_name_text_pressed, last_name_coord)
        else:
            screen.blit(last_name_text, last_name_coord)
        # Back to Main Menu button
        exit_bound = get_bound(screen, 0.25, 0.67, 0.67, 0.73)
        exit_coord = get_coord(screen, 0.25, 0.65)
        if check_mouse_hover(exit_bound, mouse):
            screen.blit(exit_text_pressed, exit_coord)
        else:
            screen.blit(exit_text, exit_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ["", 2]
            if event.type == pygame.MOUSEBUTTONDOWN:
                # First Name button
                if check_mouse_hover(first_name_bound, mouse):
                    return ["First Name", 0]
                # Middle Name button
                if check_mouse_hover(middle_name_bound, mouse):
                    return ["Middle Name", 0]
                # Last Name button
                if check_mouse_hover(last_name_bound, mouse):
                    return ["Last Name", 0]
                # Back to Menu button
                if check_mouse_hover(exit_bound, mouse):
                    return ["", 1]
        pygame.display.update()
