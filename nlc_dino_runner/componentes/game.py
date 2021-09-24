import pygame
import random
from pygame import mixer

from nlc_dino_runner.componentes.others.cloud import Cloud
from nlc_dino_runner.componentes.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.componentes.dinosaur import Dinosaur
from nlc_dino_runner.componentes.obstacles import text_utils
from nlc_dino_runner.componentes.obstacles.ObstaclesManager import ObstaclesManager
from nlc_dino_runner.componentes.obstacles.cactus import Cactus
from nlc_dino_runner.components.player_hearts.hearts_manager import HeartsManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, SMALL_CACTUS, \
    LARGE_CACTUS, RUNNING, RESET, GAME_OVER, SOUND_THEME_FOUND


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
        self.power_up_manager = PowerUpManager()
        self.hearts_manager = HeartsManager()
        self.points = 0
        self.running = True
        self.death_count = 0

        self.cloud = Cloud()

        self.max_score_points = 0

    def run(self):

        self.points = 0
        self.obstacle_manager.reset_obstacles()
        #Hacemos que al emepxar de nuevo la partidad no haya power ups
        self.power_up_manager.reset_power_ups(self.points, self.player)
        self.hearts_manager.reset_counter_hearts()
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

        self.cloud.generate_cloud(self.game_speed)

        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        if self.player.throwing_hammer:
            self.player.hammer_throwed.update_hammer(self.player)

    def draw(self):

        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        self.hearts_manager.draw(self.screen)
        self.max_score = 0

        self.cloud.draw_cloud(self.screen, self.game_speed)

        if self.player.throwing_hammer:
            self.player.hammer_throwed.draw_hammer(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        # aumentando velocidad conforme suban puntos
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.max_score_print()
        self.player.check_invencibility(self.screen)
        self.player.check_hammer(self.screen)

    def max_score_print(self):

        if self.points > self.max_score_points:
            self.max_score_points = self.points

        text, text_rect = text_utils.get_centered_message(f"Max score: {self.max_score_points}" , witdh= 855, height= 25, size = 28)
        self.screen.blit(text, text_rect)

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
        message = ""
        #aumentando funcion apra que aparesca el score a partrir de la primera muerte

        if self.death_count == 0: message = "PRESS AN KEY TO START"
        else:

            message = "PRESS AN KEY TO RESTART"

            points,points_rect = text_utils.get_centered_message("Score: "+ str(self.points), height = half_screen_height + 130)
            self.screen.blit(points,points_rect)
            self.screen.blit(RESET, ((SCREEN_WIDTH // 2) - 40, half_screen_height + 12))
            death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count), height=half_screen_height + 94)
            self.screen.blit(death_score, death_score_rect)
            self.screen.blit(GAME_OVER, ((SCREEN_WIDTH // 2) - 170, half_screen_height - 200))

        text, text_rect = text_utils.get_centered_message(message)
        self.screen.blit(text, text_rect)

        self.screen.blit(ICON, ((SCREEN_WIDTH//2)-40 , half_screen_height-150))







