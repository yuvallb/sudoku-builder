import logging

from solvers.basesolver import BaseSolver
from models.board import Board
import numpy as np

class Remaining1(BaseSolver):
    def __init__(self) -> None:
        super().__init__()

    def solve(self, board: Board) -> int:
        self._steps = 0
        self._iterations = 0
        found = True


        while found and self._steps < self._maxSteps and self._iterations < self._maxIterations:
            found = False

            vals = board.values()
            y = 0
            for row in vals:
                y += 1
                flags = np.zeros((board.dim()+1), dtype=np.bool_)
                flags[row] = True
                if flags[1:].sum() == 8:
                    missingValues = np.where(flags==False)[0]
                    missingValue = missingValues[0]
                    missingValueLocation = np.where(row==0)[0][0] + 1
                    board.fillValue(missingValueLocation,y,missingValue)
                    vals = board.values()
                    self._steps += 1
                    found = True

            if self._steps >= self._maxSteps:
                break

            x = 0
            for col in vals.T:
                x += 1
                flags = np.zeros((board.dim()+1), dtype=np.bool_)
                flags[col] = True
                if flags[1:].sum() == 8:
                    missingValues = np.where(flags==False)[0]
                    missingValue = missingValues[0]
                    missingValueLocation = np.where(col==0)[0][0] + 1
                    board.fillValue(x,missingValueLocation,missingValue)
                    vals = board.values()
                    self._steps += 1
                    found = True

            if self._steps >= self._maxSteps:
                break

            for i in range(board.dim2()):
                for j in range(board.dim2()):
                    fromI = i * board.dim2()
                    toI = fromI + board.dim2()
                    fromJ = j * board.dim2()
                    toJ = fromJ + board.dim2()
                    innerCube = vals[fromI:toI,fromJ:toJ]
                    cube = innerCube.flatten()

                    flags = np.zeros((board.dim()+1), dtype=np.bool_)
                    flags[cube] = True
                    if flags[1:].sum() == 8:
                        missingValues = np.where(flags==False)[0]
                        missingValue = missingValues[0]
                        missingValueLocation = np.where(cube==0)[0][0]
                        x = (j * board.dim2() ) + (missingValueLocation % board.dim2()) + 1
                        y = (i * board.dim2() ) + int(missingValueLocation / board.dim2()) + 1
                        board.fillValue(x,y,missingValue)
                        logging.debug("Remaining-one solver: Enter {} in ({} , {})".format(missingValue, x, y))
                        vals = board.values()
                        self._steps += 1
                        found = True
            
            self._iterations += 1
            logging.debug("Remaining-one solver finished iteration {} total found".format(self._steps))

        self._possibleValues = []
        return self._steps