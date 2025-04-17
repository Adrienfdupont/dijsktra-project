import pygame
import os
import json
from src.settings import *
from src.map import Map
from src.list import List

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        regions = json.load(open(os.path.join('assets', 'regions.json')))
        airports_data = json.load(open(os.path.join('assets', 'airports.geojson')))['features']

        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self._clock = pygame.time.Clock()
        self._running = True
        self._list = List(regions)
        self._maps = []

        for region in regions:
            filename = region['name'] + '.png'
            if os.path.exists(os.path.join('assets', 'maps', filename)):
                region_airports = []
                for airport_data in airports_data:
                    if airport_data['properties']['departement'] in region['departements']:
                        region_airports.append(airport_data)
                self._maps.append(Map(region, region_airports))

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
                    if self._list.handle_click(event.pos):
                        for map in self._maps:
                            if map.get_region()['name'] == self._list.get_selected_region():
                                map.set_visibility(True)
                            else:
                                map.set_visibility(False)
                    for map in self._maps:
                        map.handle_click(event.pos)

    def update(self):
        pass

    def draw(self):
        self._screen.fill(BG_COLOR)
        for map in self._maps:
                map.draw(self._screen)
        self._list.draw(self._screen)
        pygame.display.flip()
