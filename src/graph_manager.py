import json
import os
from src.point import Point
from src.line import Line
from src.settings import *
from src.priority_queue import PriorityQueue

class GraphManager:
    def __init__(self):
        self.points = []
        self.lines = []
        self.graph = {}

        point_json = json.load(open(os.path.join('assets', 'points.geojson')))
        for point in point_json['features']:
            pos = self.geojson_to_pygame(point['geometry']['coordinates'])
            code = point['properties']['code']
            point = Point(code, pos)
            self.points.append(point)
            self.graph[code] = {}

        line_json = json.load(open(os.path.join('assets', 'lines.geojson')))
        for line in line_json['features']:
            pos1 = self.geojson_to_pygame(line['geometry']['coordinates'][0])
            pos2 = self.geojson_to_pygame(line['geometry']['coordinates'][1])
            codes = line['properties']['codes']
            weight = line['properties']['weight']
            line = Line(codes, weight, pos1, pos2)
            self.lines.append(line)

            self.graph[codes[0]][codes[1]] = weight
            self.graph[codes[1]][codes[0]] = weight
            
        print(self.find_shortest_path('LFYG', 'LFQJ'))

    def draw(self, screen):
        for line in self.lines:
            line.draw(screen)
        for point in self.points:
            point.draw(screen)

    def geojson_to_pygame(self, coords):
        x_ratio = (coords[0] - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)
        y_ratio = (MAX_LATITUDE - coords[1]) / (MAX_LATITUDE - MIN_LATITUDE)

        x_screen = int(x_ratio * WIDTH)
        y_screen = int(y_ratio * HEIGHT)
        return x_screen, y_screen
    
    def find_shortest_path(self, start, end):
        previous = {v: None for v in self.graph.keys()}
        visited = {v: False for v in self.graph.keys()}
        distances = {v: float("inf") for v in self.graph.keys()}
        distances[start] = 0
        queue = PriorityQueue()
        queue.add_task(0, start)

        while queue:
            removed_distance, removed = queue.pop_task()
            visited[removed] = True

            for node, distance in self.graph[removed].items():
                if visited[node]:
                    continue
                new_distance = removed_distance + distance
                if new_distance < distances[node]:
                    distances[node] = new_distance
                    previous[node] = removed
                    queue.add_task(new_distance, node)
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = previous[current]
        return path