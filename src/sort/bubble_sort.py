import sort.sort as sort

import typing


class BubbleSort(sort.Sort):
    """Bubble sort is a mutli pass algorithm. This is different than insert and selection sort because the same procedure is repeated until no actions are taken.

    Each pass will switch adjacent values if they are out of place (in the context of ascending, the left value is greater than the right value).

    An additional pass without any actions is required in order to ensure that the list is in order.

    Time complexity is O(n*n), a horrible worst case scenario.

    Extra memory usage is also small O(1).
    """

    def sort(self, int_list: typing.List[int]) -> typing.List[int]:
        # Try implementing your own bubble sort by not returing the input list, triggering the test case when pytest is executed
        return int_list
