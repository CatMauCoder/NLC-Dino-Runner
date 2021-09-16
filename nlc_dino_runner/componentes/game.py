import pygame

from nlc_dino_runner.componentes.dinosaur import Dinosaur
from nlc_dino_runner.componentes.obstacles import text_utils
from nlc_dino_runner.componentes.obstacles.ObstaclesManager import ObstaclesManager
from nlc_dino_runner.componentes.obstacles.cactus import Cactus
# from nlc_dino_runner.componentes.obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, SMALL_CACTUS, \
    LARGE_CACTUS, RUNNING


class Game:
    def __init__(self):
        pygame.init()
        # Poniendo titulo al juego
        pygame.display.set_caption(TITLE)
        # Poniendo Icono
        pygame.display.set_icon(ICON)
        # Reloj de tiempo
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        # VAriables de coordenadas
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.points = 0
        self.running = True
        self.death_count = 0

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.points = 0
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            # Detentanto si se salio del programa
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):

        # Ciclos por segundo
        self.clock.tick(FPS)
        # Dibujamos el color
        self.screen.fill((255, 255, 255))
        self.score()
        # Agregando Fondo
        self.draw_background()
        # dibujando dino
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        # aumentando velocidad conforme suban puntos
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)

    def draw_background(self):
        image_width = BG.get_width()
        # AGREGANDO IMAGEN A SCREEN
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):

        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        self.print_menu_elements()

        pygame.display.update()
        self.handle_key_events_on_menu()


    def handle_key_events_on_menu(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT //2

        text, text_rect = text_utils.get_centered_message("Press an key to Star")
        self.screen.blit(text,text_rect)

        death_score, death_score_rect = text_utils.get_centered_message("Death count: "+ str(self.death_count), height = half_screen_height + 50)
        self.screen.blit(death_score, death_score_rect)

        self.screen.blit(ICON, ((SCREEN_WIDTH//2)-40 , half_screen_height-150))