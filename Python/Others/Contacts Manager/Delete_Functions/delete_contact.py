from Display_Functions.display_input import *
from Delete_Functions.delete_contact_functions import *


def delete_contact(screen):
    running = True
    while running:
        screen_width = screen.get_width()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        delete_id_text, delete_id_text_pressed = get_button('Delete By ID', font)
        delete_by_phone_text, delete_by_phone_text_pressed = get_button('Delete By Phone', font)
        exit_text, exit_text_pressed = get_button('Back to Previous Menu', font)
        mouse = pygame.mouse.get_pos()
        # Delete by ID button
        delete_id_bound = get_bound(screen, 0.33, 0.56, 0.37, 0.43)
        delete_id_coord = get_coord(screen, 0.33, 0.35)
        if check_mouse_hover(delete_id_bound, mouse):
            screen.blit(delete_id_text_pressed, delete_id_coord)
        else:
            screen.blit(delete_id_text, delete_id_coord)
        #  Delete by Phone button
        delete_phone_bound = get_bound(screen, 0.30, 0.61, 0.47, 0.53)
        delete_phone_coord = get_coord(screen, 0.30, 0.45)
        if check_mouse_hover(delete_phone_bound, mouse):
            screen.blit(delete_by_phone_text_pressed, delete_phone_coord)
        else:
            screen.blit(delete_by_phone_text, delete_phone_coord)
        # back to previous menu button
        exit_bound = get_bound(screen, 0.25, 0.67, 0.57, 0.63)
        exit_coord = get_coord(screen, 0.25, 0.55)
        if check_mouse_hover(exit_bound, mouse):
            screen.blit(exit_text_pressed, exit_coord)
        else:
            screen.blit(exit_text, exit_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Delete by ID button
                if check_mouse_hover(delete_id_bound, mouse):
                    response = display_id(screen)
                    if response[1] == 0:
                        if not delete_submit_id(response[0], screen):
                            return False
                    elif response[1] == 2:
                        return False
                # Delete by Phone button
                if check_mouse_hover(delete_phone_bound, mouse):
                    response = display_phone(screen)
                    if response[1] == 0:
                        if not delete_submit_phone(response[0].strip(), screen):
                            return False
                    elif response[1] == 2:
                        return False
                # back to main menu button
                if check_mouse_hover(exit_bound, mouse):
                    return True
        pygame.display.update()
    return True
