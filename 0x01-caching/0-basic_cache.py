#!/usr/bin/env python3
"""
Basic Cache System
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache"""
    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item from Cache"""
        if key is not None and self.cache_data.get(key):
            return self.cache_data.get(key)
        return None
