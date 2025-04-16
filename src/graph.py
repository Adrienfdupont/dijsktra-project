from src.priority_queue import PriorityQueue

class Graph:
    def __init__(self):
        self._nodes = {}

    def add_node(self, code):
        if code not in self._nodes:
            self._nodes[code] = {}

    def add_edge(self, code, edge, weight):
        if code not in self._nodes:
            self.add_node(code)
        self._nodes[code][edge] = weight
    def find_shortest_path(self, start, end):
        previous = {v: None for v in self._nodes.keys()}
        visited = {v: False for v in self._nodes.keys()}
        distances = {v: float("inf") for v in self._nodes.keys()}
        distances[start] = 0
        queue = PriorityQueue()
        queue.add_task(0, start)

        while queue:
            removed_distance, removed = queue.pop_task()
            visited[removed] = True

            for node, distance in self._nodes[removed].items():
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
    