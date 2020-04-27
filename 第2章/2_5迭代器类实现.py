"""
使用python实现一个支持任何序列类型的迭代器类
"""


class Sequencelterator():
    """An iterator for any of Python's sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence  # keep a reference to the underlying data
        self._k = -1          # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        self._k += 1          # advance to next index
        if self._k < len(self._seq):
            return self._seq[self._k]   # return the data element
        else:
            raise StopIteration()         # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    seq = Sequencelterator(nums)
    print(type(seq))
    print([x for x in seq])
