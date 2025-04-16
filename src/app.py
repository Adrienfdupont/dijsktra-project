import pygame
import os
from src.settings import *
from src.graph_manager import Graph_manager

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = pygame.image.load(os.path.join('assets', 'nord_map_945x768.png'));
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.graph_manager = Graph_manager()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.graph_manager.handle_click(event.pos)

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.screen.blit(self.background, (0, 0))
        self.graph_manager.draw(self.screen)
        pygame.display.flip()
