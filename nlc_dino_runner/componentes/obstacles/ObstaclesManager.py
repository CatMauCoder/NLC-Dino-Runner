import pygame
import random

from nlc_dino_runner.componentes import game
from nlc_dino_runner.componentes.obstacles.Bird import Bird
from nlc_dino_runner.componentes.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SOUND_GAME_OVER


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []
        self.list_obstacles = [Cactus, Bird]
        self.list_cactus = [SMALL_CACTUS, LARGE_CACTUS]


    def update(self, game):
        if len(self.obstacles_list) == 0:
            #self.obstacles_list.append(Cactus(SMALL_CACTUS))
            # CREANDO VARIABLE PARA OBTENER OBSTACULOS AL AZAR
            self.agreged_obstacle = random.choice(self.list_obstacles)

            if self.agreged_obstacle == Cactus:
                self.obstacles_list.append(Cactus(random.choice(self.list_cactus)))

            elif self.agreged_obstacle == Bird:
                self.obstacles_list.append(Bird(BIRD))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.throwing_hammer:
                if game.player.hammer_throwed.rect.colliderect(obstacle.rect):
                    self.obstacles_list.remove(obstacle)
                    #continue

            if game.player.dino_rect.colliderect(obstacle.rect):

                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    game.hearts_manager.hearts_conter -=1
                    if game.hearts_manager.hearts_conter > 0:
                        self.obstacles_list.remove(obstacle)

                    else:
                        SOUND_GAME_OVER.play()
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