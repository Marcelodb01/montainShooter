#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):



        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

