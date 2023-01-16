import logging

from solvers.basesolver import BaseSolver
from models.board import Board
import numpy as np

class EliminationRemaining(BaseSolver):
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
            if self._possibleValues != []:
                possibleValues = self._possibleValues
            
            
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
            
            #self.printPossibleValues(possibleValues,dim,vals )

            # find remaining in rows
            for y in np.arange(dim):
                counter = np.zeros(dim, dtype=np.int_)
                for x in np.arange(dim):
                    if vals[y][x] == 0:
                        counter[possibleValues[y][x]] += 1
                for x in np.arange(dim):
                    if counter[x] == 1:
                        print("Got {} in location {} , {} rows",x, x , y)
                        print(counter)

            # find remaining in rows
            for x in np.arange(dim):
                counter = np.zeros(dim, dtype=np.int_)
                for y in np.arange(dim):
                    if vals[y][x] == 0:
                        counter[possibleValues[y][x]] += 1
                for y in np.arange(dim):
                    if counter[y] == 1:
                        print("Got {} in location {} , {} cols",x, x , y)
                        print(counter)



            self._iterations += 1
            logging.debug("Elimination solver finished iteration {} total found".format(self._steps))

        self._possibleValues = possibleValues
        return self._steps

    def _inSameRow(self, x,y,px,py):
        return x != px and y == py
    def _inSameCol(self, x,y,px,py):
        return x == px and y != py
    def _inSameCube(self, x,y,px,py, dim2):
        if x == px and y == py:
            return False
        return (int(x / dim2) == int(px / dim2)) and (int(y / dim2) == int(py / dim2))

    def printPossibleValues(self, pv, dim, vals):
        for y in np.arange(dim):
            line = ''
            for x in np.arange(dim):
                if vals[y][x] == 0:
                    line = line + str(np.where(pv[y][x])[0]+1)
                else:
                    line = line  + str(vals[y][x]) 
                if x==2 or x==5:
                    line = line +' | '
                else: 
                    line = line + '|'
            print(line)
            if y == 2 or y == 5:
                print('---------------------')
