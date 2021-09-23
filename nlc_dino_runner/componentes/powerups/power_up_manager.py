import random
import pygame

from nlc_dino_runner.componentes.powerups.hammer import Hammer
from nlc_dino_runner.componentes.powerups.shield import Shield

from nlc_dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE


class PowerUpManager:

    def __init__(self):
        #creamos lista de power ups
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))

    def reset_power_ups(self, points):
        #se vacia la lsta de power ups
        self.power_ups = []
        self.points = points
        #ponemos esta variable para que aparescan cuando se tiene cierto puntaje
        self.when_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):

        self.points = points
        #comparamos si no hay power ups
        if len(self.power_ups) == 0:
            #comparamos si el puntaje ya es el establecido para qye apresca el power ups
            if self.when_appears == self.points:
                print("generating powerup")
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                #agregamos el power up
                self.power_ups.append(random.choice([Shield(), Hammer()]))

        return self.power_ups

    def update(self, points, game_speed, player):

        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    player.shield = True
                    player.show_text = True
                    player.type = power_up.type
                    time_random = random.randrange(5, 8)
                    player.shield_time_up = power_up.start_time + (time_random * 1000)

                if power_up.type == HAMMER_TYPE:
                    player.hammer = True
                    player.type = power_up.type
                    player.hammers_remain = 3

                self.power_ups.remove(power_up)

    def draw(self, screen):

        for power_up in self.power_ups:
            power_up.draw(screen)
