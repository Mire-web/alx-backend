#!/usr/bin/env python3
"""
Simple helper function to aid ease of Pagination
"""
from typing import Tuple


def index_range(page: int = 1, page_size: int = 15) -> Tuple[int, int]:
    """Return the start and end Index for a pagination"""
    if page == 1:
        return (0, page_size)
    start_index = (page * 10)
    end_index = start_index + page_size
    return (start_index, end_index)
