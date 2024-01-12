class Iterator(object):
    def __init__(self, array):
        self._array = array
        self._i = 0

    def __iter__(self):
        return self

    def __len__(self):
        return self._array.shape[0]

    def __next__(self):
        if self._i == self._array.shape[0]:
            raise StopIteration()
        x, y = self._array[self._i]
        self._i += 1
        return x, y
