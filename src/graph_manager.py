import json
import os
from src.node import Node
from src.edge import Edge
from src.settings import *
from src.priority_queue import PriorityQueue

class GraphManager:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.graph = {}

        node_json = json.load(open(os.path.join('assets', 'nodes.geojson')))
        for node in node_json['features']:
            pos = self.geojson_to_pygame(node['geometry']['coordinates'])
            code = node['properties']['code']
            self.add_node(code, pos)
            self.graph[code] = {}

        edge_json = json.load(open(os.path.join('assets', 'edges.geojson')))
        for edge in edge_json['features']:
            pos1 = self.geojson_to_pygame(edge['geometry']['coordinates'][0])
            pos2 = self.geojson_to_pygame(edge['geometry']['coordinates'][1])
            codes = edge['properties']['codes']
            weight = edge['properties']['weight']
            self.add_edge(codes, weight, pos1, pos2)

            self.graph[codes[0]][codes[1]] = weight
            self.graph[codes[1]][codes[0]] = weight
            
        print(self.find_shortest_path('LFYG', 'LFQJ'))

    def add_node(self, code, pos):
        node = Node(code, pos)
        self.nodes.append(node)
        return node

    def add_edge(self, codes, weight, pos1, pos2):
        edge = Edge(codes, weight, pos1, pos2)
        self.edges.append(edge)

    def draw(self, screen):
        for edge in self.edges:
            edge.draw(screen)
        for node in self.nodes:
            node.draw(screen)

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