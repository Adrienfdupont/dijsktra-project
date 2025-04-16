import json
import os
from src.point import Point
from src.line import Line
from src.graph import Graph
from src.settings import *

class Map:
    def __init__(self):
        self._points = []
        self._lines = []
        self._user_selected_points = []
        self._graph = Graph()

        point_json = json.load(open(os.path.join('assets', 'points.geojson')))
        for point in point_json['features']:
            pos = self.geojson_to_surface(point['geometry']['coordinates'])
            code = point['properties']['code']
            point = Point(code, pos)
            self._points.append(point)
            self._graph.add_node(code)

        line_json = json.load(open(os.path.join('assets', 'lines.geojson')))
        for line in line_json['features']:
            pos1 = self.geojson_to_surface(line['geometry']['coordinates'][0])
            pos2 = self.geojson_to_surface(line['geometry']['coordinates'][1])
            codes = line['properties']['codes']
            weight = line['properties']['weight']
            
            line = Line(codes, weight, pos1, pos2)
            self._lines.append(line)
            self._graph.add_edge(codes[0], codes[1], weight)
            self._graph.add_edge(codes[1], codes[0], weight)

    def draw(self, screen):
        for line in self._lines:
            line.draw(screen)
        for point in self._points:
            point.draw(screen)

    def geojson_to_surface(self, coords):
        x_ratio = (coords[0] - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)
        y_ratio = (MAX_LATITUDE - coords[1]) / (MAX_LATITUDE - MIN_LATITUDE)

        x_screen = int(x_ratio * WIDTH)
        y_screen = int(y_ratio * HEIGHT)
        return x_screen, y_screen
    
    def handle_click(self, pos):
        if len(self._user_selected_points) == 2:
            self.reset_point_selection()
            return

        for point in self._points:
            if point.get_x() - POINT_RADIUS <= pos[0] <= point.get_x() + POINT_RADIUS and \
               point.get_y() - POINT_RADIUS <= pos[1] <= point.get_y() + POINT_RADIUS:
                if point.get_code() not in self._user_selected_points:
                    self._user_selected_points.append(point.get_code())
                    point.set_color(SELECTED_POINT_COLOR)
                else:
                    self._user_selected_points.remove(point.get_code())
                    point.set_color(POINT_COLOR)
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
            point.set_color(POINT_COLOR)
        self._user_selected_points = []
