#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import COLOR_WRITE, WIN_HEIGHT
from code.entity import entity
from code.entityFactory import entityFactory


class Level:
    def __init__(self,window,name,game_mode):
        self.window = window
        self.name = name
        self.game_mode= game_mode
        self.entity_list: list[entity]=[]
        self.entity_list.extend(entityFactory.get_entity('Level1Bg'))
        self.entity_list.append(entityFactory.get_entity('Player1'))
        self.timeout = 20000

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock= pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf,dest= ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_text(14,f'{self.name} - timeout: {self.timeout / 1000 : 1f}s',COLOR_WRITE,(10,5) )
            self.level_text(14, f' fps: {clock.get_fps() : .1f}', COLOR_WRITE, (10,WIN_HEIGHT - 35))
            self.level_text(14, f' entidades {len(self.entity_list)}', COLOR_WRITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()


    def level_text(self, text_size:int, text:str, text_color: tuple, text_pos:tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter",size=text_size)
        text_surf: Surface = text_font.render(text, True,text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top=text_pos[1])
        self.window.blit(source=text_surf, dest= text_rect)
