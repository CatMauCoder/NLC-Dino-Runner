from nlc_dino_runner.componentes.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import HAMMER_TYPE, HAMMER, SCREEN_WIDTH, DEFAULT_TYPE

class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

    def set_pos_hammer(self, dino_rect):
        self.rect.x = dino_rect.x
        self.rect.y = dino_rect.y

    def update_hammer(self, player):
        self.rect.x += 20
        if self.rect.x > SCREEN_WIDTH:
            player.throwing_hammer = False


    def draw_hammer(self, screen):
        screen.blit(self.image, self.rect)
