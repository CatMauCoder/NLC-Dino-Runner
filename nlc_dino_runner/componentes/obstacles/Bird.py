from nlc_dino_runner.componentes.obstacles.obstacles import Obstacles
import random


class Bird(Obstacles):
    LIST_POSICION_BIRD = [185, 250]

    def __init__(self, image_bird):
        self.step_bird = 0
        self.type = 0
        super().__init__(image_bird, self.type)
        self.rect.y = random.choice(self.LIST_POSICION_BIRD)

    def update_bird(self):
        # Creando un update para hacer que se mueva

        self.step_bird += 1.2
        if self.step_bird < 5:
            self.obstacle_type = 0
        else:
            self.obstacle_type = 1

        if self.step_bird >= 10: self.step_bird = 0