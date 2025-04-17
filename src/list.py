import pygame
from src.settings import *

class List:
    def __init__(self, regions):
        self._region_items = []
        self._selected_region = None

        for region in regions:
            font = pygame.font.SysFont(None, FONT_SIZE)
            text = font.render(region['name'], True, REGION_COLOR)
            rect = text.get_rect()
            rect.center = (WIDTH - 150, 20 + len(self._region_items) * 20)
            region_item = {
                'name': region['name'],
                'surface': text,
                'rect': rect,
            }
            self._region_items.append(region_item)

    def draw(self, screen):
        for i in range(len(self._region_items)):
            region = self._region_items[i]
            if region['name'] == self._selected_region:
                region['surface'].set_alpha(255)
            else:
                region['surface'].set_alpha(128)
            screen.blit(region['surface'], region['rect'])
        
    def handle_click(self, pos):
        for region in self._region_items:
            if region['rect'].collidepoint(pos):
                self._selected_region = region['name']
                return True

    def get_selected_region(self):
        return self._selected_region