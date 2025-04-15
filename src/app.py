import pygame
import os
from src.settings import *
from src.graph_manager import GraphManager

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = pygame.image.load(os.path.join('assets', 'nord_map_945x768.png'));
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.graph = GraphManager()

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
        pass

    def draw(self):
        self.screen.fill((20, 20, 20))
        self.screen.blit(self.background, (0, 0))
        self.graph.draw(self.screen)
        pygame.display.flip()