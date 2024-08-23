from Libraries_and_Variables_Definition.checking_functions import *


def contact_added(screen):
    return text_page("Contact Added Successfully!", screen, 0.08, 0.08, 0.3)


def contact_deleted(screen):
    return text_page("Contact Deleted Successfully!", screen, 0.08, 0.08, 0.3)


def invalid_name(screen):
    return text_page("Invalid Name!", screen, 0.08, 0.23, 0.3)


def invalid_email(screen):
    return text_page("Invalid Email!", screen, 0.08, 0.23, 0.3)


def email_updated(screen):
    return text_page("Email Updated Successfully!", screen, 0.08, 0.08, 0.3)


def name_updated(screen):
    return text_page("Name Updated Successfully!", screen, 0.08, 0.08, 0.3)


def invalid_number(screen):
    return text_page("Invalid Phone!", screen, 0.08, 0.23, 0.3)


def phone_updated(screen):
    return text_page("Phone Updated Successfully!", screen, 0.08, 0.08, 0.3)


def invalid_id(screen):
    return text_page("Invalid ID!", screen, 0.08, 0.31, 0.3)


def already_exists(screen):
    return text_page("Already Exists!", screen, 0.08, 0.23, 0.3)


def no_record_found(screen):
    return text_page("No Record Found!", screen, 0.08, 0.2, 0.3)


def same_name(screen):
    return text_page("Same Name!", screen, 0.08, 0.23, 0.3)


def text_page(text, screen, font_size, x1, y1):
    running = True
    while running:
        screen_width = screen.get_width()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        text_font = pygame.font.SysFont('arial', int(screen_width * font_size))
        display_text = text_font.render(text, True, white)
        exit_text, exit_text_pressed = get_button('Back to Previous Menu', font)
        mouse = pygame.mouse.get_pos()
        # Display text
        sc_coord = get_coord(screen, x1, y1)
        screen.blit(display_text, sc_coord)
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
                # back to main menu button
                if check_mouse_hover(exit_bound, mouse):
                    return True
        pygame.display.update()
