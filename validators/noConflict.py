from models.board import Board

import numpy as np

class NoConflict:
    def validate(self, board: Board):
        self.__dim = board.dim()
        self.__dim2 = board.dim2()
        values = board.values()
        if not self._allValidRows(values):
            return False
        if not self._allValidRows(values):
            return False
        for i in range(self.__dim2):
            for j in range(self.__dim2):
                fromI = i * self.__dim2
                toI = fromI + self.__dim2
                fromJ = j * self.__dim2
                toJ = fromJ + self.__dim2
                innerCube = values[fromI:toI,fromJ:toJ]
                if not self._isValidRow(innerCube.flatten()):
                    return False
        return True

    def _allValidRows(self, board: np.ndarray):
        for row in board:
            if not self._isValidRow(row):
                return False
        return True

    def _isValidRow(self, row: np.ndarray):
        flags = np.zeros((self.__dim), dtype=np.bool_)
        for val in row:
            if val > 0:
                if flags[val-1]:
                    return False
                flags[val-1] = True
        return True
