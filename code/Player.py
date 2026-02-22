import pygame

from code.Const import ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_UP
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)       

    def move(self,):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < pygame.display.get_surface().get_height():
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_LEFT[self.name]  ] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_RIGHT[self.name] ] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass