import pygame

from nlc_dino_runner.componentes.dinosaur import Dinosaur
from nlc_dino_runner.componentes.obstacles.ObstaclesManager import ObstaclesManager
from nlc_dino_runner.componentes.obstacles.cactus import Cactus
#from nlc_dino_runner.componentes.obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, SMALL_CACTUS, \
    LARGE_CACTUS


class Game:
    def __init__(self):
        pygame.init()
        #Poniendo titulo al juego
        pygame.display.set_caption(TITLE)
        #Poniendo Icono
        pygame.display.set_icon(ICON)
        #Reloj de tiempo
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        #VAriables de coordenadas
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()

    def run(self):
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()

        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            #Detentanto si se salio del programa
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        #Ciclos por segundo
        self.clock.tick(FPS)
        #Dibujamos el color
        self.screen.fill((255, 255, 255))
        #Agregando Fondo
        self.draw_background()
        #dibujando dino
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        # AGREGANDO IMAGEN A SCREEN
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
