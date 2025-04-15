import pygame
from src.settings import *

class Point:
    def __init__(self, code, pos):
        self.code = code
        self.pos = pos

    def draw(self, screen):
        pygame.draw.circle(screen, POINT_COLOR, self.pos, POINT_RADIUS)
        font = pygame.font.SysFont(None, POINT_FONT_SIZE)
        text = font.render(str(self.code), True, POINT_FONT_COLOR)
        text_rect = text.get_rect(left=self.pos[0]+5, top=self.pos[1]+5)
        screen.blit(text, text_rect)