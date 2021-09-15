# from Python Crash Course

# Image by <a href="https://pixabay.com/users/dawnydawny-2157612/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2442125">dawnydawny</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2442125">Pixabay</a>

import pygame

class Ship:
    def __init__(self, ai_game):
        '''initialize the ship and set its starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.settings = ai_game.settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        #store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''update the ship's position based on the movement flag'''
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)