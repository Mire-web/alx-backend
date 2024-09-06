#!/usr/bin/env python3
"""
Basic Caching system in python
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching"""
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
            most_recent = len(self.__accessed_keys) - 1
            self.modifyArray(self.__accessed_keys, key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.__accessed_keys[most_recent])
                if key != self.__accessed_keys[most_recent]:
                    formatted_text = self.__accessed_keys[most_recent]
                    print("DISCARD: {}".format(formatted_text))
                self.__accessed_keys.pop(most_recent)
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.modifyArray(self.__accessed_keys, key)
        return self.cache_data.get(key)
