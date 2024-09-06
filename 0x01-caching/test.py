#!/usr/bin/python3
"""
Test
"""
import sys

try:
    FIFOCache = __import__('1-fifo_cache').FIFOCache

    my_cache = FIFOCache()
    my_cache.print_cache()
    my_cache.put("test1", "myValue")
    my_cache.print_cache()
    if my_cache.get(None) is not None:
        print("get must return None if the key is None")
    else:
        print("OK")
    if my_cache.get("test2") is not None:
        print("test2 doesn't exist in the cache, get must return None")
    else:
        print("OK")
except:
    print(sys.exc_info()[1])
