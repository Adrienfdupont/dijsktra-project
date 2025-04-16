import pygame
from src.settings import *

class Line(pygame.sprite.Sprite):
    def __init__(self, codes, weight, pos1, pos2):
        super().__init__()
        self._codes = codes
        self._pos1 = pos1
        self._pos2 = pos2
        self._weight = weight
        self._color = LINE_COLOR

        font = pygame.font.SysFont(None, FONT_SIZE)
        self._text = font.render(str(self._weight), True, self._color)
        self._text_rect = self._text.get_rect(center=(
            (self._pos1[0] + self._pos2[0]) // 2, (self._pos1[1] + self._pos2[1]) // 2
        ))

        self._text_bg = pygame.Surface(self._text_rect.size)
        self._text_bg.fill(FONT_BG_COLOR)
        self._text_bg_rect = pygame.Rect(self._text_rect)
        self._text_bg_rect.center = self._text_rect.center

    def draw(self, screen):
        pygame.draw.line(screen, self._color, self._pos1, self._pos2, LINE_WIDTH)
        screen.blit(self._text_bg, self._text_bg_rect)
        screen.blit(self._text, self._text_rect)
    
    def set_color(self, color):
        self._color = color
        self._font = pygame.font.SysFont(None, FONT_SIZE)
        self._text = self._font.render(str(self._weight), True, color)

    def get_codes(self):
        return self._codes
    