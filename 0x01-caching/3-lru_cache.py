#!/usr/bin/env python3
"""
Basic Caching system in python
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""
    def __init__(self):
        """initialize class data"""
        super().__init__()
        self.__accessed_keys = []

    def modifyArray(self, keys, key):
        """Modify used keys array"""
        if key in keys:
            keys.pop(keys.index(key))
        keys.append(key)

    def put(self, key, item):
        """Put into the cache"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.__accessed_keys[0])
                if key != self.__accessed_keys[0]:
                    print("DISCARD: {}".format(self.__accessed_keys[0]))
                self.__accessed_keys.pop(0)
            self.modifyArray(self.__accessed_keys, key)
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.modifyArray(self.__accessed_keys, key)
        return self.cache_data.get(key)
