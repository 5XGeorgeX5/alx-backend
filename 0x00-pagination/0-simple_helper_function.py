#!/usr/bin/env python3
"""Define the index_range function"""


def index_range(page, page_size):
    """
    returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
