#!/usr/bin/python3
""" FIFO caching module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ puts an item in cache_data """
        if key is None or item is None:
            return
        if (len(self.cache_data) == self.MAX_ITEMS):
            removed = self.cache_data.popitem(last=False)
            print(f"DISCARD: {removed[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """ gets an item from cache_data """
        return self.cache_data.get(key, None)
