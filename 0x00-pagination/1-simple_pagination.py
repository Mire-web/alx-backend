#!/usr/bin/env python3
"""
Simple helper function to aid ease of Pagination
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int = 1, page_size: int = 15) -> Tuple[int, int]:
    """Return the start and end Index for a pagination"""
    return ((page - 1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get Page"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start_index, end_index = index_range(page, page_size)
        try:
            return self.dataset()[start_index: end_index]
        except IndexError:
            return []
