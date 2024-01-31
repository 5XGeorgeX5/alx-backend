#!/usr/bin/python3
""" LIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """

    def put(self, key, item):
        """ puts an item in cache_data """
        if key is None or item is None:
            return
        if (len(self.cache_data) == self.MAX_ITEMS):
            removed = self.cache_data.popitem()
            print(f"DISCARD: {removed[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """ gets an item from cache_data """
        return self.cache_data.get(key, None)
