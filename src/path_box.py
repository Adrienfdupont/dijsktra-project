import pygame
from src.settings import *

class Path_box:
    def __init__(self):
        self._path = []

    def set_path(self, path):
        self._path = path

    def draw(self, screen):
        font = pygame.font.SysFont(None, FONT_SIZE)
        text = font.render('\n'.join(self._path), True, POINT_COLOR)
        text_rect = text.get_rect(left=0, top=HEIGHT - 200)
        screen.blit(text, text_rect)