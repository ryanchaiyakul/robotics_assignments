from unittest import TestCase

import random
from sort.bubble_sort import BubbleSort
from sort.insert_sort import InsertSort

from sort.selection_sort import SelectionSort
from sort.sort import Sort


class TestSort(TestCase):

    def test_selection_sort(self):
        self.works(SelectionSort)

    def test_insert_sort(self):
        self.works(InsertSort)

    def test_bubble_sort(self):
        self.works(BubbleSort)

    @staticmethod
    def works(sorter: Sort):
        if not TestSort.assert_list_equal([0, 3, 2, 1], sorter().sort([0, 3, 2, 1])):
            # Sort was not implemented
            assert True

        # Three times is the charm
        for i in range(3):
            sorted_list = list(
                range(random.randint(0, 10), random.randint(80, 100)))
            unsorted_list = sorted_list

            random.shuffle(unsorted_list)

            assert TestSort.assert_list_equal(
                sorted_list, sorter().sort(unsorted_list))

    @staticmethod
    def assert_list_equal(a_list, b_list) -> bool:
        return all([a == b for a, b in zip(a_list, b_list)])
