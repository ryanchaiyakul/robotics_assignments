import typing
import sort.sort as sort


class InsertSort(sort.Sort):
    """Insertion sort iterates over a list and moves the values to the left until it is larger than the value to the 'left'.

    Time complexity is also O(n^2) because of the nested for loop.

    Extra memory usage is O(1).
    """

    def sort(self, int_list: typing.List[int]) -> typing.List[int]:
        # Does not need to start at the first value b/c it's already all the way to the left
        for i in range(1, len(int_list)):
            value = int_list[i]

            # Start comparing with the value to the left
            j = i-1
            # You can also write j >= 0
            # Compare the current value with the values to the left and move everything to the left until it is greater
            while j > -1 and value < int_list[j]:
                int_list[j + 1] = int_list[j]
                j -= 1
        return int_list
