import pygame
from src.settings import *
import os

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((MAP_WIDTH + 20, MAP_HEIGHT + 20))
        self.clock = pygame.time.Clock()
        self.running = True
        self.surface = pygame.image.load(os.path.join('assets', 'nord_map_945x768.png'));
        self.surface = pygame.transform.scale(self.surface, (MAP_WIDTH, MAP_HEIGHT))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # à remplir plus tard

    def draw(self):
        self.screen.fill((20, 20, 20))
        self.screen.blit(self.surface, (10, 10))
        pygame.display.flip()