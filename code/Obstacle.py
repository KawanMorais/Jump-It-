#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED_OBSTACLE
from code.Entity import Entity

class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED_OBSTACLE # O obstáculo terá uma velocidade constante

    def move(self, ):
        # Obstáculo se move da direita para a esquerda
        self.rect.centerx -= self.speed
        pass