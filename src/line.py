import pygame
from src.settings import *

class Line:
    def __init__(self, codes, weight, pos1, pos2):
        self._codes = codes
        self._weight = weight
        self._pos1 = pos1
        self._pos2 = pos2
        self._color = LINE_COLOR

    def draw(self, screen):
        pygame.draw.line(screen, self._color, self._pos1, self._pos2, LINE_WIDTH)
        font = pygame.font.SysFont(None, LINE_FONT_SIZE)
        text = font.render(str(self._weight), True, self._color)
        text_rect = text.get_rect(center=((self._pos1[0] + self._pos2[0]) // 2, (self._pos1[1] + self._pos2[1]) // 2))
        
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

    def get_codes(self):
        return self._codes
    