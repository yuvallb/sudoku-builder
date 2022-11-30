import logging

from solvers.basesolver import BaseSolver
from models.board import Board
import numpy as np

class Elimination(BaseSolver):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, board: Board) -> int:
        dim = board.dim()
        dim2 = board.dim2()
        found = True
        self._steps = 0
        self._iterations = 0

        while found and self._steps < self._maxSteps and self._iterations < self._maxIterations:

            found = False
            vals = board.values()
            possibleValues = np.ones((dim,dim,dim),dtype=np.bool_)
            
            # eliminating values
            for x in np.arange(dim):
                for y in np.arange(dim):
                    if vals[y][x] > 0:
                        for px in np.arange(dim):
                            for py in np.arange(dim):
                                if self._inSameCol(x,y,px,py):
                                    possibleValues[py][px][vals[y][x]-1] = False
                                if self._inSameRow(x,y,px,py):
                                    possibleValues[py][px][vals[y][x]-1] = False
                                if self._inSameCube(x,y,px,py, dim2):
                                    possibleValues[py][px][vals[y][x]-1] = False

            # filling values back to board
            for x in np.arange(dim):
                for y in np.arange(dim):
                    if vals[y][x] == 0:
                        if possibleValues[y][x].sum() == 1:
                            missingValue = np.where(possibleValues[y][x])[0][0] + 1
                            board.fillValue(x+1, y+1, missingValue)
                            vals = board.values()
                            logging.debug("Elimination solver: Enter {} in ({} , {})".format(missingValue, x+1, y+1))
                            self._steps += 1
                            found = True

            self._iterations += 1
            logging.debug("Elimination solver finished iteration {} total found".format(self._steps))

        return self._steps

    def _inSameRow(self, x,y,px,py):
        return x != px and y == py
    def _inSameCol(self, x,y,px,py):
        return x == px and y != py
    def _inSameCube(self, x,y,px,py, dim2):
        if x == px and y == py:
            return False
        return (int(x / dim2) == int(px / dim2)) and (int(y / dim2) == int(py / dim2))