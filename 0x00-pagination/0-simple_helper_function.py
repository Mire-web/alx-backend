#!/usr/bin/env python3
"""
Simple helper function to aid ease of Pagination
"""
from typing import Tuple


def index_range(page: int = 1, page_size: int = 15) -> Tuple[int, int]:
    """Return the start and end Index for a pagination"""
    return ((page - 1) * page_size, page_size * page)
