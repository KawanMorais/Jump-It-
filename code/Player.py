#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.key

from .Const import GROUND_Y
from .Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.animation_frames = []  # Lista para armazenar as superfícies de cada frame
        self.current_frame = 0  # Índice do frame atual da animação
        self.animation_speed = 0.1  # Velocidade da animação

        self.last_update = pygame.time.get_ticks() # Tempo do último update do frame

        self.frame_width = 32  # Largura de um frame individual
        self.frame_height = 32  # Altura de um frame individual
        self.num_frames = 8  # Número total de frames no file

        # Carrega e recorta os frames da sprite sheet
        self.load_frames()

        self.surf = self.animation_frames[self.current_frame]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.rect.bottom = GROUND_Y + 32 # Garante que o player esteja no chão

        self.is_jumping = False  # Flag para saber se o jogador está pulando
        self.vertical_speed = 0  # Velocidade vertical (positiva para cair, negativa para subir)
        self.gravity = 0.5  # Força da gravidade (quanto maior, mais rápido ele cai)
        self.jump_strength = -10  # Força inicial do pulo (negativa para ir para cima)

    def load_frames(self):
        for i in range(self.num_frames):
            frame_rect = pygame.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height)
            frame_surf = self.surf.subsurface(frame_rect).copy()
            self.animation_frames.append(frame_surf)

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:  # animation_speed * 1000 para converter segundos para milissegundos
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.surf = self.animation_frames[self.current_frame]

    def move(self, ):
        if self.is_jumping:
            self.rect.y += self.vertical_speed  # Aplica a velocidade vertical à posição Y
            self.vertical_speed += self.gravity  # A gravidade aumenta a velocidade vertical
            if self.rect.y >= GROUND_Y:
                self.rect.y = GROUND_Y    # Garante que ele pouse exatamente no chão
                self.is_jumping = False         # O pulo terminou
                self.vertical_speed = 0         # Reseta a velocidade vertical

        self.update_animation()