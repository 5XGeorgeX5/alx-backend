#!/usr/bin/env python3
""" LFU caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_map = {}

    def put(self, key, item):
        """ puts an item in cache_data """
        if key is None or item is None:
            return
        if (len(self.cache_data) == self.MAX_ITEMS):
            min_freq = min(self.cache_map, key=self.cache_map.get)
            self.cache_data.pop(min_freq)
            print(f"DISCARD: {min_freq}")
            self.cache_map.pop(min_freq)
        if key not in self.cache_map:
            self.cache_map[key] = 0
        self.cache_data[key] = item

    def get(self, key):
        """ gets an item from cache_data """
        if key is None or key not in self.cache_data:
            return None
        self.cache_map[key] += 1
        return self.cache_data[key]
