#!/usr/bin/env python3

from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    """represents a cache using the FIFO algo"""

    def __init__(self):
        """initializes the cache"""
        super().__init___()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > 4:
            key, value = self.cache_data.popitem(False)
            print("DISCARD: ", key)

    def get(self, key):
        """retrieves an item from cached items"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
