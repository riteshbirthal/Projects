import random
from user_input import *


def computer_gesture():
    gestures = ["Rock", "Paper", "Scissor"]
    return gestures[random.randint(0, 2)]


def enter_game(screen, background_colour, running):
    gesture = str(user_gesture_input(screen, background_colour))
    comp_gesture = computer_gesture()
    win_txt = str(predict_result(gesture, comp_gesture))
    while running:
        screen_width, screen_height = screen.get_width(), screen.get_height()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width * 0.07))
        mouse = pygame.mouse.get_pos()

        # go to main menu button
        main_menu_text = font.render('Go to Main Menu', True, white)
        main_menu_text_pressed = font.render('Go to Main Menu', True, (100, 150, 200))
        menu_button_coord = (screen_width * 0.25, screen_height * 0.62)
        main_bound = [[screen_width * 0.25, screen_width * 0.75], [screen_height * 0.62, screen_height * 0.73]]
        if main_bound[0][0] <= mouse[0] <= main_bound[0][1] and main_bound[1][0] <= mouse[1] <= main_bound[1][1]:
            screen.blit(main_menu_text_pressed, menu_button_coord)
        else:
            screen.blit(main_menu_text, menu_button_coord)

        # restart button
        restart_text = font.render('Restart Game', True, (255, 255, 255))
        restart_text_pressed = font.render('Restart Game', True, (100, 150, 200))
        restart_button_coord = (screen_width * 0.3, screen_height * 0.75)
        res_bound = [[screen_width * 0.25, screen_width * 0.75], [screen_height * 0.75, screen_height * 0.85]]
        if res_bound[0][0] <= mouse[0] <= res_bound[0][1] and res_bound[1][0] <= mouse[1] <= res_bound[1][1]:
            screen.blit(restart_text_pressed, restart_button_coord)

        else:
            screen.blit(restart_text, restart_button_coord)

        # your and computer inputs
        input_font = pygame.font.SysFont('arial', int(screen_width * 0.05))
        input_ = input_font.render("You : " + gesture + "  |  " + "Computer : " + comp_gesture, True, white)
        input_coord = (screen_width * 0.2, screen_height * 0.2)
        screen.blit(input_, input_coord)

        # game output
        win_font = pygame.font.SysFont('arial', int(screen_width * 0.15))
        win_text = win_font.render(win_txt, True, white)
        lose_text = win_font.render(win_txt, True, (255, 0, 0))
        output_text_coord = (screen_width * 0.2, screen_height * 0.33)
        if win_txt == "You Won!":
            screen.blit(win_text, output_text_coord)
        else:
            screen.blit(lose_text, output_text_coord)

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                running = False
                restart = False
                return running, restart
            if event.type == pygame.MOUSEBUTTONDOWN:
                # main menu button
                if main_bound[0][0] <= mouse[0] <= main_bound[0][1] and \
                        main_bound[1][0] <= mouse[1] <= main_bound[1][1]:
                    restart = False
                    return running, restart
                # restart button
                if res_bound[0][0] <= mouse[0] <= res_bound[0][1] and res_bound[1][0] <= mouse[1] <= res_bound[1][1]:
                    restart = True
                    return running, restart
        pygame.display.update()