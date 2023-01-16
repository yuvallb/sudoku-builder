import logging

from solvers.basesolver import BaseSolver
from models.board import Board
import numpy as np

class Placement(BaseSolver):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, board: Board) -> int:
        dim = board.dim()
        dim2 = board.dim2()
        vals = board.values()
        found = True
        self._steps = 0
        self._iterations = 0

        while found and self._steps < self._maxSteps and self._iterations < self._maxIterations:
            found = False

            # iterate over rows:
            for y in np.arange(dim):
                row = vals[y]
                for candidateValue in np.arange(dim)+1:
                    if candidateValue in row:
                        continue
                    flags = np.ones((dim), dtype=np.bool_)
                    for x in np.arange(dim):
                        if row[x] > 0:
                            flags[x] = False
                        elif self._colHasValue(vals, x, candidateValue):
                            flags[x] = False
                        elif self._cubeHasValue(vals, x, y, candidateValue, dim2):
                            flags[x] = False
                    if flags.sum() == 1:
                        Xlocation = np.where(flags)[0][0] + 1
                        board.fillValue(Xlocation, y + 1, candidateValue)
                        logging.debug("Placement solver (rows): Enter {} in ({} , {})".format(candidateValue, Xlocation, y+1))
                        vals = board.values()
                        self._steps += 1
                        found = True

            if self._steps >= self._maxSteps:
                break

            # iterate over columns:
            for x in np.arange(dim):
                col = vals.T[x]
                for candidateValue in np.arange(dim)+1:
                    if candidateValue in col:
                        continue
                    flags = np.ones((dim), dtype=np.bool_)
                    for y in np.arange(dim):
                        if col[y] > 0:
                            flags[y] = False
                        elif self._rowHasValue(vals, y, candidateValue):
                            flags[y] = False
                        elif self._cubeHasValue(vals, x, y, candidateValue, dim2):
                            flags[y] = False
                    if flags.sum() == 1:
                        Ylocation = np.where(flags)[0][0] + 1
                        board.fillValue(x+1, Ylocation, candidateValue)
                        logging.debug("Placement solver (cols): Enter {} in ({} , {})".format(candidateValue, x+1, Ylocation))
                        vals = board.values()
                        self._steps += 1
                        found = True
             
            if self._steps >= self._maxSteps:
                break

            # iterate over inner cubes:
            for i in range(dim2):
                for j in range(dim2):
                    fromI = i * dim2
                    toI = fromI + dim2
                    fromJ = j * dim2
                    toJ = fromJ + dim2
                    innerCube = vals[fromI:toI,fromJ:toJ]
                    cube = innerCube.flatten()

                    for candidateValue in np.arange(dim)+1:
                        if candidateValue in cube:
                            continue
                        flags = np.ones((dim), dtype=np.bool_)
                        for c in np.arange(dim):
                            if cube[c] > 0:
                                flags[c] = False
                            elif self._rowHasValue(vals, (i*dim2) + int(c / dim2), candidateValue):
                                flags[c] = False
                            elif self._colHasValue(vals, (j*dim2) + (c % dim2), candidateValue):
                                flags[c] = False
                        if flags.sum() == 1:
                            CubeLocation = np.where(flags)[0][0]
                            Ylocation = (i*dim2) + int(CubeLocation / dim2) + 1
                            Xlocation = (j*dim2) + (CubeLocation % dim2) + 1
                            board.fillValue(Xlocation, Ylocation, candidateValue)
                            logging.debug("Placement solver (cube): Enter {} in ({} , {})".format(candidateValue, Xlocation, Ylocation))
                            vals = board.values()
                            self._steps += 1
                            found = True

            self._iterations += 1
            logging.debug("Placement solver finished iteration {} total found".format(self._steps))

        self._possibleValues = []
        return self._steps

    def _colHasValue(self, vals, x, pv):
        return pv in vals.T[x]
    def _rowHasValue(self, vals, y, pv):
        return pv in vals[y]
    def _cubeHasValue(self, vals, x, y, pv, dim2):
        fromX = int(x / dim2) * dim2
        toX = fromX + dim2
        fromY = int(y / dim2) * dim2
        toY = fromY + dim2
        innerCube = vals[fromY:toY,fromX:toX]
        return pv in innerCube