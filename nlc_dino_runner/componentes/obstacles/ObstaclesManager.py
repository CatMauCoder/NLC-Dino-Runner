import pygame

from nlc_dino_runner.componentes import game
from nlc_dino_runner.componentes.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)