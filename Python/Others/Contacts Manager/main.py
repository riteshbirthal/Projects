from Create_Functions.create_contact import *
from Delete_Functions.delete_contact import *
from Edit_Functions.edit_contact import *
from Search_Functions.search_contact import *
from Read_Write_Functions.read_write import *


def application_start():
    read_data()
    flags = pygame.RESIZABLE
    screen = pygame.display.set_mode((600, 400), flags)
    pygame.display.set_caption('Phone-Book Manager Application')
    running = True
    while running:
        screen_width = screen.get_width()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width*0.05))
        create_contact_text, create_contact_text_pressed = get_button('Create New Contact', font)
        search_contact_text, search_contact_text_pressed = get_button('Search Contact', font)
        edit_contact_text, edit_contact_text_pressed = get_button('Edit Contact', font)
        delete_contact_text, delete_contact_text_pressed = get_button('Delete Contact', font)
        exit_text, exit_text_pressed = get_button('Exit Application', font)
        mouse = pygame.mouse.get_pos()
        # create contact button
        create_contact_bound = get_bound(screen, 0.30, 0.60, 0.27, 0.33)
        create_contact_coord = get_coord(screen, 0.30, 0.25)
        if check_mouse_hover(create_contact_bound, mouse):
            screen.blit(create_contact_text_pressed, create_contact_coord)
        else:
            screen.blit(create_contact_text, create_contact_coord)
        # search contact button
        search_contact_bound = get_bound(screen, 0.33, 0.61, 0.37, 0.43)
        search_contact_coord = get_coord(screen, 0.33, 0.35)
        if check_mouse_hover(search_contact_bound, mouse):
            screen.blit(search_contact_text_pressed, search_contact_coord)
        else:
            screen.blit(search_contact_text, search_contact_coord)
        # edit contact button
        edit_contact_bound = get_bound(screen, 0.36, 0.57, 0.47, 0.53)
        edit_contact_coord = get_coord(screen, 0.36, 0.45)
        if check_mouse_hover(edit_contact_bound, mouse):
            screen.blit(edit_contact_text_pressed, edit_contact_coord)
        else:
            screen.blit(edit_contact_text, edit_contact_coord)
        # delete contact button
        delete_contact_bound = get_bound(screen, 0.33, 0.61, 0.57, 0.63)
        delete_contact_coord = get_coord(screen, 0.33, 0.55)
        if check_mouse_hover(delete_contact_bound, mouse):
            screen.blit(delete_contact_text_pressed, delete_contact_coord)
        else:
            screen.blit(delete_contact_text, delete_contact_coord)
        # exit button
        exit_bound = get_bound(screen, 0.33, 0.6, 0.67, 0.73)
        exit_coord = get_coord(screen, 0.33, 0.65)
        if check_mouse_hover(exit_bound, mouse):
            screen.blit(exit_text_pressed, exit_coord)
        else:
            screen.blit(exit_text, exit_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # create contact button
                if check_mouse_hover(create_contact_bound, mouse):
                    running = create_contact(screen)
                # search contact button
                if check_mouse_hover(search_contact_bound, mouse):
                    running = search_contact(screen)
                # edit contact button
                if check_mouse_hover(edit_contact_bound, mouse):
                    running = edit_contact(screen)
                # delete contact button
                if check_mouse_hover(delete_contact_bound, mouse):
                    running = delete_contact(screen)
                # exit button
                if check_mouse_hover(exit_bound, mouse):
                    running = False
        pygame.display.update()


if __name__ == '__main__':
    print("Application Start...")
    application_start()
    write_data()
    print("Application Stopped..")
