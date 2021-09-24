import pygame

from nlc_dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.tff'
BLACK_COLOR = (0, 0, 0)

def get_score_element(points):
    #Pongo SysFont porque no m reconoce solo el Font para instanciar a la fuente
    font = pygame.font.SysFont(FONT_STYLE , 28)

    text = font.render("Points: " + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1020, 25)
    return (text, text_rect)

def get_centered_message(message, witdh = SCREEN_WIDTH//2 , height = SCREEN_HEIGHT//2, size = 30):

    font = pygame.font.SysFont(FONT_STYLE , size)

    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (witdh , height)
    return(text, text_rect)
