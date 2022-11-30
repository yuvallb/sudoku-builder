from models.board import Board
from numpy import ndarray

class ISolver:
    def solve(self, board: Board) -> int:
        pass

    def limitSteps(maxSteps: int):
        pass

    def limitSteps(maxIterations: int):
        pass

    def getSteps() -> int:
        pass
    
    def getIterations() -> int:
        pass
    
    def getRemainingPossibleValues() -> ndarray:
        pass

    def setPreviousPossibleValues(pv: ndarray):
        pass