from nlc_dino_runner.componentes.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)
