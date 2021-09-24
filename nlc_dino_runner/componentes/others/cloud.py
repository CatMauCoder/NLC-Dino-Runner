import random

from pygame.sprite import Sprite

from nlc_dino_runner.componentes import game
from nlc_dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Sprite):

    #LIST_POSICION_Y = [150 ,]

    def __init__(self,):
        self.image = CLOUD
        self.rect_cloud = self.image.get_rect()
        self.rect_cloud.x = SCREEN_WIDTH
        self.rect_cloud.y = random.randint(100, 160)
        #self.speed_cloud = game_speed - 10
        self.list_cloud = []
        self.generate = random.randint(50, 90)
        self.conter_second = 0

    def generate_cloud(self, game_speed):
             #aumentando valor de conter second

        self.conter_second += 1

        if self.conter_second == self.generate:
           self.list_cloud.append(Cloud())

           self.generate = random.randint(50, 135)
           self.conter_second = 0

    def draw_cloud(self,screen,game_speed):
        if len(self.list_cloud) > 0:
            for cloud in self.list_cloud:

                cloud.rect_cloud.x -= 3
                screen.blit(cloud.image , cloud.rect_cloud)
                if cloud.rect_cloud.x < -SCREEN_WIDTH:
                    self.list_cloud.remove(cloud)








