import pygame
from src.settings import *

class Point(pygame.sprite.Sprite):
    def __init__(self, code, pos):
        super().__init__()
        self._code = code

        font = pygame.font.SysFont(None, FONT_SIZE)
        self._text = font.render(self._code, True, FONT_COLOR)
        self._text_rect = self._text.get_rect(center=pos)

        self._text_bg = pygame.Surface(self._text_rect.size)
        self._text_bg.fill(FONT_BG_COLOR)
        self._text_bg_rect = pygame.Rect(self._text_rect)
        self._text_bg_rect.center = self._text_rect.center

    def draw(self, screen):
        screen.blit(self._text_bg, self._text_bg_rect)
        screen.blit(self._text, self._text_rect)

    def set_color(self, color):
        self._font = pygame.font.SysFont(None, FONT_SIZE)
        self._text = self._font.render(self._code, True, color)

    def get_code(self):
        return self._code
    
    def get_left(self):
        return self._text_rect.left
    
    def get_top(self):
        return self._text_rect.top
    
    def get_right(self):
        return self._text_rect.right
    
    def get_bottom(self):
        return self._text_rect.bottom
