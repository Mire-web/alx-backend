#!/usr/bin/env python3
"""
Basic Caching system in python
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching"""
    def __init__(self):
        """initialize class data"""
        super().__init__()
        self.__accessed_keys = []

    def modifyArray(self, keys, key):
        """Modify used keys array"""
        count = 0
        for obj in keys:
            if key == obj['key']:
                count = obj['count'] + 1
                keys.pop(keys.index(obj))
        keys.append({'key': key, 'count': count})

    def put(self, key, item):
        """Put into the cache"""
        if key is None or item is None:
            pass
        else:
            self.modifyArray(self.__accessed_keys, key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.__accessed_keys[0]['key'])
                if key != self.__accessed_keys[0]['key']:
                    formatted_text = self.__accessed_keys[0]['key']
                    print("DISCARD: {}".format(formatted_text))
                self.__accessed_keys.pop(0)
            self.cache_data[key] = item

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.modifyArray(self.__accessed_keys, key)
        return self.cache_data.get(key)
