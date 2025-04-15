import pygame
from src.settings import *

class Line:
    def __init__(self, codes, weight, pos1, pos2):
        self.id = codes
        self.weight = weight
        self.pos1 = pos1
        self.pos2 = pos2

    def draw(self, screen):
        pygame.draw.line(screen, LINE_COLOR, self.pos1, self.pos2, LINE_WIDTH)
        font = pygame.font.SysFont(None, LINE_FONT_SIZE)
        text = font.render(str(self.weight), True, LINE_FONT_COLOR)
        text_rect = text.get_rect(center=((self.pos1[0] + self.pos2[0]) // 2, (self.pos1[1] + self.pos2[1]) // 2))
        
        background_rect = pygame.Rect(
            text_rect.left,
            text_rect.top,
            text_rect.width,
            text_rect.height
        )
        pygame.draw.rect(screen, LINE_FONT_BG_COLOR, background_rect)
        
        screen.blit(text, text_rect)