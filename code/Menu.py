#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, WIN_HEIGHT


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu2.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, high_score: int):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Jump", COLOR_ORANGE, ((WIN_WIDTH/2), 70) )
            self.menu_text(50, "It!", COLOR_ORANGE, ((WIN_WIDTH/2 + 5), 120) )

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2) , 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2) , 200 + 30 * i))

            high_score_display_text = f"HIGH SCORE: {high_score}"
            high_score_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=20)
            high_score_surf = high_score_font.render(high_score_display_text, True, C_WHITE)
            high_score_rect = high_score_surf.get_rect(center=(WIN_WIDTH / 2, 200 + 30 * len( MENU_OPTION) + 50))
            self.window.blit(high_score_surf, high_score_rect)

            pygame.display.flip()

        # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygameD
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        if MENU_OPTION[menu_option] == 'SCORE':
                            self.show_high_score_screen(high_score)
                        else:
                            return MENU_OPTION[menu_option]

    def show_high_score_screen(self, high_score: int):
        # Exibe uma tela dedicada com o high score.
        while True:
            self.window.fill((0, 0, 0))


            self.menu_text(40, "HIGHSCORE", C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50))

            # Exibe o score
            score_text = f"Highscore: {high_score}"
            self.menu_text(30, score_text, C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 20))

            # Instrução para voltar
            self.menu_text(20, "Pressione qualquer tecla para voltar", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 100))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    return  # Sai desta tela e volta para o menu principal



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)