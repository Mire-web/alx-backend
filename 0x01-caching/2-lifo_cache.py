#!/usr/bin/env python3
"""
Basic Caching system in python
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching"""
    def __init__(self):
        """initialize class data"""
        super().__init__()

    def put(self, key, item):
        """Put into the cache"""
        if key is None or item is None:
            pass
        else:
            if self.cache_data.get(key):
                self.cache_data.pop(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, value = self.cache_data.popitem()
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
