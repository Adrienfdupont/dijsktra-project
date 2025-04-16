import itertools
from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self._pq = []
        self._entry_finder = {}
        self._counter = itertools.count()

    def __len__(self):
        return len(self._pq)

    def add_task(self, priority, task):
        'Add a new task or update the priority of an existing task'
        if task in self._entry_finder:
            self.update_priority(priority, task)
            return self
        count = next(self._counter)
        entry = [priority, count, task]
        self._entry_finder[task] = entry
        heappush(self._pq, entry)

    def update_priority(self, priority, task):
        'Update the priority of a task in place'
        entry = self._entry_finder[task]
        count = next(self._counter)
        entry[0], entry[1] = priority, count

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self._pq:
            priority, count, task = heappop(self._pq)
            del self._entry_finder[task]
            return priority, task
        raise KeyError('pop from an empty priority queue')