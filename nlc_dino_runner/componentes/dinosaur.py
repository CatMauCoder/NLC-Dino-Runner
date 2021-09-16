#Importanto clas Sprite
import pygame
from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import RUNNING, DUCKING, JUMPING


class Dinosaur(Sprite):
    # Coordenadas
    x_pos = 80
    y_pos = 310
    y_POS_DUCK = 340
    JUMP_VEL = 8

    def __init__(self):
        self.image = RUNNING[0]
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

            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False

        elif not self.dino_jump:

            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):

        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 2

    def duck(self):

        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_POS_DUCK
        self.step_index += 1

    def jump(self):

        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 5
            self.jump_vel -= 1

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.y_pos
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen):
        # funcion blit para dibujar
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))