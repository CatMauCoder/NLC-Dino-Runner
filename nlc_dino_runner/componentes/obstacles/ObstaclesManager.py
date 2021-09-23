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
            if game.player.throwing_hammer:
                if game.player.hammer_throwed.rect.colliderect(obstacle.rect):
                    self.obstacles_list.remove(obstacle)

            if game.player.dino_rect.colliderect(obstacle.rect):

                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    game.hearts_manager.hearts_conter -=1
                    if game.hearts_manager.hearts_conter > 0:
                        self.obstacles_list.remove(obstacle)

                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count +=1
                        #REINICIAMDO LA VELOCIDAD
                        game.game_speed = 20
                        break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []