import pygame

from code.Menu import Menu
from code.Level import Level
from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        #pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):         
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in MENU_OPTION[0:3]: # NEW GAME 1P
                level = Level(self.window, 'Level1', menu_return)
                menu_return = level.run()

            elif menu_return == MENU_OPTION[4]: 
                pygame.quit()
                exit()
                
            else:
                pass