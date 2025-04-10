import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDH
from code.entity import entity


class player(entity):

    def __init__(self, name, position: tuple):
       super().__init__(name, position)

    def update(self,):
        pass

    def move(self,):
        pressed_key= pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
                self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass


