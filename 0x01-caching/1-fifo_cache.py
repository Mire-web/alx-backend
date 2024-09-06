#!/usr/bin/env python3
"""
Basic Caching system in python
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put into the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = list(self.cache_data.keys())[0]
                self.cache_data.pop(discarded)
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
