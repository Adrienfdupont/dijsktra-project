import pygame
import os
import random
from src.point import Point
from src.line import Line
from src.graph import Graph
from src.settings import *

class Map:
    def __init__(self, region, aiports_data):
        self._region = region
        self._visible = False
        
        filename = region['name'] + '.png'
        self._background = pygame.image.load(os.path.join('assets', 'maps', filename));
        bg_width, bg_height = self._background.get_size()
        scale_factor = HEIGHT / max(bg_width, bg_height)
        new_width = int(bg_width * scale_factor)
        new_height = int(bg_height * scale_factor)
        self._background = pygame.transform.scale(self._background, (new_width, new_height))
        
        self._points = pygame.sprite.Group()
        self._lines = pygame.sprite.Group()
        self._user_selected_points = []
        self._graph = Graph()

        for airport_data in aiports_data:
            if airport_data['properties']['important'] == False and self._region['name'] == 'France':
                continue
            pos = self.geojson_to_surface(airport_data['geometry']['coordinates'])
            code = airport_data['properties']['code']
            airport_sprite = Point(code, pos)
            self._points.add(airport_sprite)
            self._graph.add_node(code)

            for other_airport_data in aiports_data:
                if airport_data['properties']['code'] != other_airport_data['properties']['code']:
                    pos1 = pos
                    pos2 = self.geojson_to_surface(other_airport_data['geometry']['coordinates'])
                    codes = (airport_data['properties']['code'], other_airport_data['properties']['code'])
                    
                    distance = ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5
                    
                    weight = int(distance / 10)
                    
                    if weight > 10 and self._region['name'] == 'France':
                        continue
                    line = Line(codes, weight, pos1, pos2)
                    self._lines.add(line)
                    self._graph.add_edge(codes[0], codes[1], weight)
                    self._graph.add_edge(codes[1], codes[0], weight)

    def draw(self, screen):
        if self._visible:
            screen.blit(self._background, (0, 0))
            for line in self._lines:
                line.draw(screen)
            for point in self._points:
                point.draw(screen)

    def geojson_to_surface(self, point_coords):
        coords = self._region['coordinates']
        x_ratio = (point_coords[0] - coords['min_longitude']) / (coords['max_longitude'] - coords['min_longitude'])
        y_ratio = (coords['max_latitude'] - point_coords[1]) / (coords['max_latitude'] - coords['min_latitude'])

        x_screen = int(x_ratio * self._background.get_width())
        y_screen = int(y_ratio * self._background.get_height())
        return x_screen, y_screen
    
    def handle_click(self, pos):
        if len(self._user_selected_points) == 2:
            self.reset_point_selection()
            return

        for point in self._points:
            if point.get_left() < pos[0] < point.get_right() and point.get_top() < pos[1] < point.get_bottom():
                if point.get_code() not in self._user_selected_points:
                    self._user_selected_points.append(point.get_code())
                    point.set_color(SELECTED_POINT_COLOR)
                else:
                    self._user_selected_points.remove(point.get_code())
                    point.set_color(FONT_COLOR)
                break
        if len(self._user_selected_points) == 2:
            self.show_shortest_path()        

    def show_shortest_path(self):
        path = self._graph.find_shortest_path(self._user_selected_points[0], self._user_selected_points[1])
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            for line in self._lines:
                if start in line.get_codes() and end in line.get_codes():
                    line.set_color(PATH_LINE_COLOR)

    def reset_point_selection(self):
        for line in self._lines:
            line.set_color(LINE_COLOR)
        for point in self._points:
            point.set_color(FONT_COLOR)
        self._user_selected_points = []

    def get_region(self):
        return self._region

    def set_visibility(self, visible):
        self._visible = visible

    def get_visibility(self):
        return self._visible