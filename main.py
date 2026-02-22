import pygame


pygame.init() # Adicione isso (ESSENCIAL)
pygame.mixer.init()

from code.Game import Game

game = Game()
game.run()