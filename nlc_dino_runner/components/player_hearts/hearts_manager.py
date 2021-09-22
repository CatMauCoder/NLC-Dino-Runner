from nlc_dino_runner.components.player_hearts.hearts import Hearts
from nlc_dino_runner.utils.constants import HEARTS_COUNTER


class HeartsManager:
    def __init__(self):
        self.hearts_conter = HEARTS_COUNTER

    def draw(self, screen):
        x_position = 10

        for hearts in range(self.hearts_conter):
            heart = Hearts(x_position)
            x_position += 30
            heart.draw(screen)


    def reset_counter_hearts(self):
        self.hearts_conter = HEARTS_COUNTER



