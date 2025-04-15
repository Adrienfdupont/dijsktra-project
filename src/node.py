import pygame
from src.settings import *

class Node:
    def __init__(self, code, pos):
        self.code = code
        self.pos = pos

    def draw(self, screen):
        pygame.draw.circle(screen, NODE_COLOR, self.pos, NODE_RADIUS)
        font = pygame.font.SysFont(None, NODE_FONT_SIZE)
        text = font.render(str(self.code), True, NODE_FONT_COLOR)
        text_rect = text.get_rect(left=self.pos[0]+5, top=self.pos[1]+5)
        screen.blit(text, text_rect)