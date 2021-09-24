# Importanto clas Sprite
import pygame
from pygame.sprite import Sprite
from nlc_dino_runner.componentes.obstacles import text_utils
from nlc_dino_runner.componentes.obstacles.text_utils import get_centered_message
from nlc_dino_runner.componentes.powerups.hammer import  Hammer
from nlc_dino_runner.utils.constants import (
    RUNNING,
    DUCKING,
    JUMPING,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    DUCKING_HAMMER,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAMMER_TYPE,
    RUNNING_HAMMER,
    JUMPING_HAMMER, HAMMER, SHIELD, SOUND_JUMP
)

class Dinosaur(Sprite):
    # Coordenadas
    x_pos = 80
    y_pos = 295
    y_POS_DUCK = 340
    JUMP_VEL = 8

    def __init__(self):
        self.run_img = {
            DEFAULT_TYPE: RUNNING,
            SHIELD_TYPE: RUNNING_SHIELD,
            HAMMER_TYPE: RUNNING_HAMMER
        }

        self.jump_img = {
            DEFAULT_TYPE: JUMPING,
            SHIELD_TYPE: JUMPING_SHIELD,
            HAMMER_TYPE: JUMPING_HAMMER
        }

        self.duck_img = {
            DEFAULT_TYPE: DUCKING,
            SHIELD_TYPE: DUCKING_SHIELD,
            HAMMER_TYPE: DUCKING_HAMMER
        }

        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]

        self.shield = False
        self.shield_time_up = 0
        self.show_text = False

        self.hammer = False
        self.throwing_hammer = False
        self.hammers_remain = 3



        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL


    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()

        if user_input[pygame.K_DOWN] and not self.dino_jump:

            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False

        elif user_input[pygame.K_UP] and not self.dino_jump:

            SOUND_JUMP.play()
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False

        elif not self.dino_jump:

            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False


        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_SPACE] and self.hammer and not self.throwing_hammer:
            self.hammer_throwed = Hammer()
            self.hammer_throwed.set_pos_hammer(self.dino_rect)
            self.throwing_hammer = True
            self.hammers_remain -= 1


    def run(self):

        self.image = self.run_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def duck(self):

        self.image = self.duck_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_POS_DUCK
        self.step_index += 2

    def jump(self):


        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 5
            self.jump_vel -= 1

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.y_pos
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def check_invencibility(self,screen):

      if self.shield:
        time_to_show = round((self.shield_time_up - pygame.time.get_ticks())/ 1000,1)
        if time_to_show < 0:
            self.shield = False
            if self.type == SHIELD_TYPE:
                self.type = DEFAULT_TYPE
        else:
            if self.show_text:
                text, text_rect = text_utils.get_centered_message(
                    f"Shield enable for {time_to_show}",
                    witdh = 500,
                    height = 25,
                    size =  30)
                screen.blit(text, text_rect)

                screen.blit(SHIELD, (610, 4))

    def check_hammer(self, screen):

        if self.hammer:

            if self.hammers_remain <= 0:
                self.hammer = False
                if self.type == HAMMER_TYPE:
                    self.type = DEFAULT_TYPE
            else:

                if self.show_text:
                    text, text_rect = get_centered_message(
                        f'Hammers remain: {self.hammers_remain}',
                        witdh = 500,
                        height = 25,
                        size = 30
                    )
                    screen.blit(text, text_rect)

                    screen.blit(HAMMER, (595, 4))

    def draw(self, screen):
        # funcion blit para dibujar
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
