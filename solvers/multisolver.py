import logging

from solvers.basesolver import BaseSolver
from models.board import Board
from solvers.remaining1 import Remaining1
from solvers.elimination import Elimination
from solvers.placement import Placement
from solvers.eliminationcouples import EliminationCouples

import numpy as np

class MultiSolver(BaseSolver):

    def __init__(self) -> None:
        super().__init__()
        self._eliminator = Elimination()
        self._placer = Placement()
        self._remaining1 = Remaining1()
        self._eliminator2 = EliminationCouples()
        
    def solve(self, board: Board) -> int:
        found = True
        self._steps = 0
        self._iterations = 0

        while found and self._steps < self._maxSteps and self._iterations < self._maxIterations:

            found = False

            foundSolver = self._remaining1.solve(board)
            if foundSolver > 0:
                found = True
                self._steps += foundSolver

            if self._steps >= self._maxSteps:
                break

            foundSolver = self._eliminator.solve(board)
            if foundSolver > 0:
                found = True
                self._steps += foundSolver

            if self._steps >= self._maxSteps:
                break

            foundSolver = self._placer.solve(board)
            if foundSolver > 0:
                found = True
                self._steps += foundSolver

            if self._steps >= self._maxSteps:
                break

            foundSolver = self._eliminator2.solve(board)
            if foundSolver > 0:
                found = True
                self._steps += foundSolver

            self._iterations += 1
            logging.debug("Multi solver finished iteration {} total found".format(self._steps))


        return self._steps
