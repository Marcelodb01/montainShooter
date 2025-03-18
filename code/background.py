from code.const import WIN_WIDH, ENTITY_SPEED
from code.entity import entity


class background(entity):

    def __init__(self,name: str, position: tuple):
        super().__init__(name, position)


    def move(self,):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left= WIN_WIDH
        pass
