from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, BIRD


#Clase Padre

class Obstacles(Sprite):

    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type #el tipo de obstaculo
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH #1100

    def update(self, game_speed, obstacle_list):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacle_list.pop()

    def draw(self, screen):
        if self.image == BIRD : self.update_bird()

        screen.blit(self.image[self.obstacle_type], self.rect)