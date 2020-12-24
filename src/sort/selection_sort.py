import typing
import sort.sort


class SelectionSort(sort.Sort):
    """Selection sort iterates over the list and moves the smallest value to the front every iteration. 

    The time complexity is o(n^2) because of the nested for loops. 

    A beneficial part of this sorting algorithm is its lack of extra memory usage of O(1).
    """

    def sort(self, int_list: typing.List[int]) -> typing.List[int]:
        for i in range(len(int_list)):
            # index will store the index of the lowest value remaining in the list
            # set to the first valid index
            index = i

            # iterate over all remaining values and replace index if int_list[j] is lesser
            for j in range(i+1, len(int_list)):
                if int_list[j] < int_list[index]:
                    index = j

            # swap the 'first' and lowest value
            int_list[i], int_list[index] = int_list[index], int_list[i]

        return int_list
