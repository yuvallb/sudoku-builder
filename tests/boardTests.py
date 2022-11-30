import sys
sys.path.append('.')

from models.board import Board
from boards.examplesDim9 import ExamplesDim9

class BoardTests:
    def _testInitBoard(self):
        b = Board(9)
        b.populate(ExamplesDim9().empty)
        print(b.values())
        b.populate(ExamplesDim9().full1)
        print(b.values())

    def run(self):
        self._testInitBoard()


BoardTests().run()