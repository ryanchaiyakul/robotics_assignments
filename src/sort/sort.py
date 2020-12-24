from abc import ABCMeta, abstractmethod
import typing


class Sort(metaclass=ABCMeta):
    """Sorting algorithms will sort an integer list in ascending order.
    """

    @abstractmethod
    def sort(self, int_list: typing.List[int]) -> typing.List[int]:
        """returns the integer list in sorted ascending order.
        """
        pass
