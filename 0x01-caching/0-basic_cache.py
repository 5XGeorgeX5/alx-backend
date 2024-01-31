#!/usr/bin/python3
""" base caching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """
    def put(self, key, item):
        """ puts an item in cache_data """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ gets an item from cache_data """
        return self.cache_data.get(key, None)
