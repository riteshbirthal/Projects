from Search_Functions.search_name import *
from Search_Functions.search_contact_functions import *


def search_contact(screen):
    running = True
    while running:
        screen_width = screen.get_width()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        search_name_text, search_name_text_pressed = get_button('Search By Name', font)
        search_email_text, search_email_text_pressed = get_button('Search By Email', font)
        search_by_contact_text, search_by_contact_text_pressed = get_button('Search By Phone', font)
        exit_text, exit_text_pressed = get_button('Back to Main Menu', font)
        mouse = pygame.mouse.get_pos()
        # search by name button
        search_name_bound = get_bound(screen, 0.30, 0.60, 0.37, 0.43)
        search_name_coord = get_coord(screen, 0.30, 0.35)
        if check_mouse_hover(search_name_bound, mouse):
            screen.blit(search_name_text_pressed, search_name_coord)

        else:
            screen.blit(search_name_text, search_name_coord)
        #  search by email button
        search_email_bound = get_bound(screen, 0.30, 0.6, 0.47, 0.53)
        search_email_coord = get_coord(screen, 0.30, 0.45)
        if check_mouse_hover(search_email_bound, mouse):
            screen.blit(search_email_text_pressed, search_email_coord)
        else:
            screen.blit(search_email_text, search_email_coord)
        # search by contact button
        search_phone_bound = get_bound(screen, 0.30, 0.61, 0.57, 0.63)
        search_phone_coord = get_coord(screen, 0.30, 0.55)
        if check_mouse_hover(search_phone_bound, mouse):
            screen.blit(search_by_contact_text_pressed, search_phone_coord)
        else:
            screen.blit(search_by_contact_text, search_phone_coord)
        # exit button
        exit_bound = get_bound(screen, 0.28, 0.62, 0.67, 0.73)
        exit_coord = get_coord(screen, 0.28, 0.65)
        if check_mouse_hover(exit_bound, mouse):
            screen.blit(exit_text_pressed, exit_coord)

        else:
            screen.blit(exit_text, exit_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # search by name button
                if check_mouse_hover(search_name_bound, mouse):
                    response = search_name(screen)
                    if response[1] == 0:
                        if search_fun(response[0], screen) is False:
                            return False
                    elif response[1] == 2:
                        return False
                # search by email button
                if check_mouse_hover(search_email_bound, mouse):
                    if search_fun("Email", screen) is False:
                        return False
                # search by contact button
                if check_mouse_hover(search_phone_bound, mouse):
                    if search_fun("Phone", screen) is False:
                        return False
                # back to main menu button
                if check_mouse_hover(exit_bound, mouse):
                    return True
        pygame.display.update()
