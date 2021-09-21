import random

from pygame.sprite import Sprite

from nlc_dino_runner.utils.constants import SCREEN_HEIGHT


class PowerUp(Sprite):

      def __init__(self, image, type):
          #Atributos necesarios
          self.image = image
          self.rect = self.image.get_rect()
          self.type = type
          self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
          self.rect.y = random.randint(100, 150)

      def draw(self, screen):
          screen.blit(self.image, self.rect)

      def update(self, game_speed, powerups):
          self.rect.x -= game_speed
          #Eliminamos el POwer up cuando se pasa el borde la pantalla
          if self.rect.x < -self.rect.width:
              powerups.pop()