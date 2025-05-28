import sys
from ship import Ship
import pygame
from settings import Settings
class AlienInvasion:
        def __init__(self):
                pygame.init()
                #self.screen=pygame.display.set_mode((800,800))
                #pygame.display.set_caption("Alien Invasion")
                self.settings=Settings()
                self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
                #self.bg_color=(230,230,230)
		self.ship=Ship(self)
        def run_game(self):
                while True:
                        for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                        sys.exit()
                        self.screen.fill(self.settings.bg_color)
			self.ship.blitme()
                        pygame.display.flip()
if __name__ == '__main__':
        ai=AlienInvasion()
        ai.run_game()
