from typing import Any, Optional
from collections import OrderedDict 


class LRUCache:
    '''
    A least Recently used (LRU) cache.
    - Holds up to 'item_limit' entries,
    - Access is Tracked on 'has', 'get', and 'set' ,
    - When limit is reached, evicts the least recently used entry.
    '''

    def __init__(self, item_limit: int):
        if item_limit <= 0:
            raise ValueError("item_limit must be positive")
        self.item_limit = item_limit
        self.cache = OrderedDict

    def has(self, key: str) -> bool:
        if key in self.cache:
            self.cache.move_to_end(key)
            return True
        return False

    def get(self, key: str) -> Optional[Any]:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key] 

    def set(self, key: str, value: Any):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.item_limit:
                self.cache.popitem(last=False)
            self.cache[key] = value          