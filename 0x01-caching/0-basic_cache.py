#!/usr/bin/env python3
"""Caching module"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Represents and object for storing
       and retrieving from cache"""

       def put(self, key, item):
           '''adds an item to the cache'''
           if key is None or item is None:
               return
           self.cache_data[key] = item

       def get(self, key):
           ''' retrieves a cached item'''
           if key is None:
               return None
           return self.cache_data.get(key)
