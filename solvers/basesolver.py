from solvers.isolver import ISolver
from models.board import Board
import numpy as np

class BaseSolver(ISolver):
    def __init__(self) -> None:
        self._maxSteps = 2 ** 20
        self._maxIterations = 2 ** 20
        
        
    def solve(self, board: Board) -> int:
        self._steps = 0
        self._iterations = 0
        dim = board.dim()
        self._possibleValues = np.ones((dim,dim,dim),dtype=np.bool_)
        return self._steps

    def limitSteps(self, maxSteps: int):
        self._maxSteps = maxSteps

    def limitSteps(self, maxIterations: int):
        self._maxIterations = maxIterations

    def getSteps(self) -> int:
        return self._steps
    
    def getIterations(self) -> int:
        return self._iterations
    
    def getRemainingPossibleValues(self) -> np.ndarray:
        return np.copy(self._possibleValues)

    def setPreviousPossibleValues(self, possibleValues: np.ndarray):
        self._possibleValues = np.copy(possibleValues)
