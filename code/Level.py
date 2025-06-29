#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, GROUND_Y, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Obstacle import Obstacle
from code.Player import Player


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.player = EntityFactory.get_entity('Player', (40, GROUND_Y))
        self.entity_list.append(self.player)


        self.obstacle_spawn_time = 0  # Tempo para o próximo spawn de obstáculo
        self.min_spawn_interval = 1500  # Mínimo intervalo entre obstáculos (ms)
        self.max_spawn_interval = 3000  # Máximo intervalo entre obstáculos (ms)
        self.last_spawn_time = pygame.time.get_ticks()  # Tempo do último spawn

        self.game_over = False

        # SCORE
        self.score = 0
        self.start_time = pygame.time.get_ticks()  # Registra o tempo de início do jogo

    def run(self):
        pygame.mixer_music.load(f'asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()


        while True:
            if self.game_over:
                self.window.fill((0, 0, 0))


                self.level_text(30, "GAME OVER!", (255, 0, 0), (WIN_WIDTH / 2 - 90, WIN_HEIGHT / 2 - 20))
                self.level_text(20, f"Score: {self.score}", C_WHITE, (WIN_WIDTH / 2 - 60, WIN_HEIGHT / 2 + 35))
                self.level_text(18, "Pressione ENTER para REINICIAR ou ESC para o MENU", C_WHITE,(WIN_WIDTH / 2 - 280, WIN_HEIGHT / 2 + 70))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pygame.mixer_music.play(-1)
                            return "restart"
                        elif event.key == pygame.K_ESCAPE:
                            return "menu"
                continue


            clock.tick(60)
            current_time = pygame.time.get_ticks()

            self.score = (current_time - self.start_time) // 100

            # --- Geração de Obstáculos ---
            if current_time - self.last_spawn_time >= self.obstacle_spawn_time:
                # Gera um novo obstáculo
                new_obstacle = EntityFactory.get_entity('Obstacle1', (WIN_WIDTH, GROUND_Y))  # <--- Passa GROUND_Y
                self.entity_list.append(new_obstacle)

                # Define o tempo para o próximo spawn
                self.obstacle_spawn_time = random.randint(self.min_spawn_interval, self.max_spawn_interval)
                self.last_spawn_time = current_time

            entities_to_keep = []
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, Obstacle):
                    if self.player.rect.colliderect(ent.rect):
                            print("Colisão!")
                            self.game_over = True # Define o estado do jogo como Game Over
                            pygame.mixer.music.stop()

                # Remoção de obstáculos que saíram da tela
                if isinstance(ent, Obstacle) and ent.rect.right < 0:
                    continue
                # Se não for um obstáculo que saiu da tela, mantenha-o
                entities_to_keep.append(ent)

            # Atualiza a lista de entidades removendo os obstáculos fora da tela
            self.entity_list = entities_to_keep


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Detecta quando uma tecla é pressionada
                    if event.key == pygame.K_SPACE:  # Se a tecla ESPAÇO for pressionada
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and not ent.is_jumping:
                                ent.is_jumping = True
                                ent.vertical_speed = ent.jump_strength
                                break

            self.level_text(14, f'"{self.name}"', C_WHITE, (10, 5))
            self.level_text(14, f'Score: {self.score}', C_WHITE, (10, 25))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

