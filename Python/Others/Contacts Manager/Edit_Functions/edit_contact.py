from Edit_Functions.edit_functions import *
from Search_Functions.search_contact import *


def edit_contact(screen):
    running = True
    while running:
        screen_width = screen.get_width()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        edit_name_text, edit_name_text_pressed = get_button('Edit Name', font)
        edit_email_text, edit_email_text_pressed = get_button('Edit Email', font)
        edit_phone_text, edit_phone_text_pressed = get_button('Edit Phone', font)
        exit_text, exit_text_pressed = get_button('Back to Main Menu', font)
        mouse = pygame.mouse.get_pos()
        # Edit Name button
        edit_name_bound = get_bound(screen, 0.33, 0.52, 0.37, 0.43)
        edit_name_coord = get_coord(screen, 0.33, 0.35)
        if check_mouse_hover(edit_name_bound, mouse):
            screen.blit(edit_name_text_pressed, edit_name_coord)
        else:
            screen.blit(edit_name_text, edit_name_coord)
        # Edit Email button
        edit_email_bound = get_bound(screen, 0.33, 0.52, 0.47, 0.53)
        edit_email_coord = get_coord(screen, 0.33, 0.45)
        if check_mouse_hover(edit_email_bound, mouse):
            screen.blit(edit_email_text_pressed, edit_email_coord)
        else:
            screen.blit(edit_email_text, edit_email_coord)
        # edit phone number button
        edit_phone_bound = get_bound(screen, 0.33, 0.53, 0.57, 0.63)
        edit_phone_coord = get_coord(screen, 0.33, 0.55)
        if check_mouse_hover(edit_phone_bound, mouse):
            screen.blit(edit_phone_text_pressed, edit_phone_coord)
        else:
            screen.blit(edit_phone_text, edit_phone_coord)
        # back to main menu button
        exit_bound = get_bound(screen, 0.26, 0.61, 0.67, 0.73)
        exit_coord = get_coord(screen, 0.26, 0.65)
        if check_mouse_hover(exit_bound, mouse):
            screen.blit(exit_text_pressed, exit_coord)
        else:
            screen.blit(exit_text, exit_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # edit name button
                if check_mouse_hover(edit_name_bound, mouse):
                    response = display_id(screen)
                    if response[1] == 0:
                        if check_id(response[0]):
                            person = display_names(screen, response[1])
                            if person[1] == 0:
                                if name_valid(person[0].first_name, person[0].middle_name, person[0].last_name):
                                    if edit_submit_name(person[0], screen, int(response[0].strip())) is False:
                                        return False
                                else:
                                    if invalid_name(screen) is False:
                                        return False
                            elif person[1] == 2:
                                return False
                        else:
                            if invalid_id(screen) is False:
                                return False
                    elif response[1] == 2:
                        return False
                # edit email button
                if check_mouse_hover(edit_email_bound, mouse):
                    response = display_id(screen)
                    if response[1] == 0:
                        if check_id(response[0]):
                            id_ = int(response[0].strip())
                            response_email = display_email(screen, id_)
                            if response_email[1] == 0:
                                if email_valid(response_email[0]):
                                    if edit_submit_email(response_email[0], screen, id_) is False:
                                        return False
                            elif response_email[1] == 2:
                                return False
                        else:
                            if invalid_id(screen) is False:
                                return False
                    elif response[1] == 2:
                        return False
                # edit phone number button
                if check_mouse_hover(edit_phone_bound, mouse):
                    response = display_id(screen)
                    if response[1] == 0:
                        if check_id(response[0]):
                            id_ = int(response[0].strip())
                            response_phone = display_phone_id(screen, id_)
                            if response_phone[1] == 0:
                                if phone_valid(response_phone[0]):
                                    if edit_submit_phone(response_phone[0], screen, id_) is False:
                                        return False
                            elif response_phone[1] == 2:
                                return False
                        else:
                            if invalid_id(screen) is False:
                                return False
                    elif response[1] == 2:
                        return False
                if check_mouse_hover(exit_bound, mouse):
                    return True
        pygame.display.update()
