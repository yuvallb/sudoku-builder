import numpy as np

class Board:

    def __init__(self, dim: int) -> None:
       # if dim != 9:
       #     raise Exception("Currently supports only 9x9 boards")

        self.__dtype = np.ubyte
        if self.__dtype(dim) != dim:
            raise Exception("Board dimension should be unsigned byte (0-255)")
        self.__dim = dim
        self.__dim2 = self.__dtype(np.sqrt(dim))
        if not self.__dim2 ** 2 == self.__dim:
            raise Exception("Board dimension should squared")

        self.__values = np.zeros((self.__dim,self.__dim), dtype=self.__dtype)

    def dim(self) -> int:
        return int(self.__dim)
    def dim2(self) -> int:
        return int(self.__dim2)
    def values(self) -> np.ndarray:
        return np.copy(self.__values)

    def fillValue(self, x, y, val):
        self._validateDim(x)
        self._validateDim(y)
        self._validateValue(val)
        self.__values[y-1][x-1] = val
        return

    def populate(self, values: np.ndarray):
        adjustedValues = np.array(values, dtype=self.__dtype)
        if adjustedValues.shape != self.__values.shape:
            raise Exception("Populate shape mismatch")
        if adjustedValues.max() > self.__dim:
            raise Exception("Populate values exceed {}".format(self.__dim))
        self.__values = adjustedValues

    def _validateDim(self, val):
        if val < 1 or val > self.__dim:
            raise Exception("Dimension {} should be between 1 and {}".format(val, self.__dim))
    def _validateValue(self, val):
        if val < 0 or val > self.__dim:
            raise Exception("Value {} should be between 0 and {}".format(val, self.__dim))

