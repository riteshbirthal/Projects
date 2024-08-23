from output_window import *


def start_game():
    background_colour = (20, 100, 200)
    flags = pygame.RESIZABLE
    screen = pygame.display.set_mode((600, 400), flags)
    pygame.display.set_caption('Rock-Paper-Scissor Game')
    running = True
    restart = False
    while running:
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        screen.fill(background_colour)
        font = pygame.font.SysFont('arial', int(screen_width*0.07))
        start_text = font.render('Start Game', True, (255, 255, 255))
        start_text_pressed = font.render('Start Game', True, (100, 150, 200))
        exit_text = font.render('Quit Game', True, (255, 255, 255))
        exit_text_pressed = font.render('Quit Game', True, (100, 150, 200))
        mouse = pygame.mouse.get_pos()
        # start game button
        st_bound = [[screen_width * 0.3, screen_width * 0.7], [screen_height * 0.35, screen_height * 0.45]]
        start_coord = (screen_width * 0.36, screen_height * 0.35)
        if st_bound[0][0] <= mouse[0] <= st_bound[0][1] and st_bound[1][0] <= mouse[1] <= st_bound[1][1]:
            screen.blit(start_text_pressed, start_coord)

        else:
            screen.blit(start_text, start_coord)

        # exit button
        ex_bound = [[screen_width * 0.3, screen_width * 0.7], [screen_height * 0.5, screen_height * 0.6]]
        ex_coord = (screen_width * 0.36, screen_height * 0.5)
        if ex_bound[0][0] <= mouse[0] <= ex_bound[0][1] and ex_bound[1][0] <= mouse[1] <= ex_bound[1][1]:
            screen.blit(exit_text_pressed, ex_coord)

        else:
            screen.blit(exit_text, ex_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start button
                if st_bound[0][0] <= mouse[0] <= st_bound[0][1] and st_bound[1][0] <= mouse[1] <= st_bound[1][1]:
                    running, restart = enter_game(screen, background_colour, running)

                # exit button
                if ex_bound[0][0] <= mouse[0] <= ex_bound[0][1] and ex_bound[1][0] <= mouse[1] <= ex_bound[1][1]:
                    running = False
        if restart:
            running, restart = enter_game(screen, background_colour, running)
        pygame.display.update()