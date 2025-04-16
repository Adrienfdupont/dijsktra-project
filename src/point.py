import pygame
from src.settings import *

class Point:
    def __init__(self, code, pos):
        self._code = code
        self.pos = pos
        self._color = POINT_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, self.pos, POINT_RADIUS)
        font = pygame.font.SysFont(None, POINT_FONT_SIZE)
        text = font.render(str(self._code), True, self._color)
        text_rect = text.get_rect(left=self.pos[0]+5, top=self.pos[1]+5)

        background_rect = pygame.Rect(
            text_rect.left - 1,
            text_rect.top - 1,
            text_rect.width + 2,
            text_rect.height + 2
        )
        pygame.draw.rect(screen, FONT_BG_COLOR, background_rect)

        screen.blit(text, text_rect)
    
    def set_color(self, color):
        self._color = color

    def get_code(self):
        return self._code
    
    def get_x(self):
        return self.pos[0]
    
    def get_y(self):
        return self.pos[1]