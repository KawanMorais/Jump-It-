#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from .Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.is_jumping = False  # Flag para saber se o jogador está pulando
        self.jump_height = 100  # Altura máxima do pulo (em pixels)
        self.initial_y = position[1]  # Posição Y inicial do jogador (o chão)
        self.vertical_speed = 0  # Velocidade vertical (positiva para cair, negativa para subir)
        self.gravity = 0.5  # Força da gravidade (quanto maior, mais rápido ele cai)
        self.jump_strength = -10  # Força inicial do pulo (negativa para ir para cima)

    def move(self, ):
        if self.is_jumping:
            self.rect.y += self.vertical_speed  # Aplica a velocidade vertical à posição Y
            self.vertical_speed += self.gravity  # A gravidade aumenta a velocidade vertical
            if self.rect.y >= self.initial_y:
                self.rect.y = self.initial_y    # Garante que ele pouse exatamente no chão
                self.is_jumping = False         # O pulo terminou
                self.vertical_speed = 0         # Reseta a velocidade vertical
        pass