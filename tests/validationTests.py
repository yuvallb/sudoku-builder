import numpy as np

import sys
sys.path.append('.')

from models.board import Board
from validators.noConflict import NoConflict
from boards.examplesDim9 import ExamplesDim9

class ValidationTests:
    def _testNoConflictValidator(self):
        validator = NoConflict()
        examples = ExamplesDim9()
        full1Bad = np.array(examples.full1)
        full1Bad[0][0] = full1Bad[0][1]
        testCases = [
            ["Empty", examples.empty, True],
            ["Easy", examples.easy1, True],
            ["Full", examples.full1, True],
            ["Full bad", full1Bad, False],
        ]
        for testCase in testCases:
            (name, values, expected) = testCase
            b = Board(9)
            b.populate(values)
            actual = validator.validate(b)
            result = 'Pass' if actual == expected else 'Fail'
            print("{}: case: {} expected {} got {}".format(result, name, expected, actual))

    def run(self):
        self._testNoConflictValidator()


ValidationTests().run()