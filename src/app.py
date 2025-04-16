import pygame
import os
from src.settings import *
from src.map import Map

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._clock = pygame.time.Clock()
        self._running = True

        self._background = pygame.image.load(os.path.join('assets', 'nord_map_945x768.png'));
        self._background = pygame.transform.scale(self._background, (WIDTH, HEIGHT))

        self._map = Map()

    def run(self):
        while self._running:
            self.handle_events()
            self.update()
            self.draw()
            self._clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._map.handle_click(event.pos)

    def update(self):
        pass

    def draw(self):
        self._screen.fill(BG_COLOR)
        self._screen.blit(self._background, (0, 0))
        self._map.draw(self._screen)
        pygame.display.flip()
