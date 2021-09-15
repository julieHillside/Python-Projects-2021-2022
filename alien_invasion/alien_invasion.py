## from Python Crash Course

import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    '''Overall class to manage game assets and behavior'''
    
    def __init__(self):
        pygame.init()
        
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion Game")
        
        self.ship = Ship(self)
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
    def _check_events(self):
        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()