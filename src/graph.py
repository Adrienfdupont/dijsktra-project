from src.priority_queue import PriorityQueue

class Graph:
    def __init__(self):
        self._graph = {}

    def add_node(self, code):
        if code not in self._graph:
            self._graph[code] = {}

    def add_edge(self, code, edge, weight):
        if code not in self._graph:
            self.add_node(code)
        self._graph[code][edge] = weight
    def find_shortest_path(self, start, end):
        previous = {v: None for v in self._graph.keys()}
        visited = {v: False for v in self._graph.keys()}
        distances = {v: float("inf") for v in self._graph.keys()}
        distances[start] = 0
        queue = PriorityQueue()
        queue.add_task(0, start)

        while queue:
            removed_distance, removed = queue.pop_task()
            visited[removed] = True

            for node, distance in self._graph[removed].items():
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
            print(path)
        return path
    