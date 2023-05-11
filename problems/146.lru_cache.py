from collections import OrderedDict

"""
    Solution: Implementation with ordereddictionary
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.data:
            self.data.move_to_end(key)
        return self.data.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key not in self.data and len(self.data) == self.capacity:
            self.data.popitem(last=False)
        elif key in self.data: 
            self.data.move_to_end(key)
        self.data.update({key: value})