import numpy as np

import logging
import sys
sys.path.append('.')

from models.board import Board
from validators.noConflict import NoConflict
from boards.examplesDim9 import ExamplesDim9
from solvers.remaining1 import Remaining1
from solvers.elimination import Elimination
from solvers.eliminationremaining import EliminationRemaining
from solvers.eliminationcouples import EliminationCouples
from solvers.placement import Placement
from solvers.multisolver import MultiSolver

class SolverTests:

    def _testRemaining1Row(self):
        solver = Remaining1()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testRemaining1RowsCols(self):
        solver = Remaining1()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        b.fillValue(1,2,0)
        b.fillValue(3,3,0)
        b.fillValue(4,4,0)
        b.fillValue(5,5,0)
        b.fillValue(1,8,0)
        b.fillValue(2,8,0)
        b.fillValue(3,8,0)
        b.fillValue(4,8,0)
        b.fillValue(7,8,0)
        b.fillValue(8,8,0)
        b.fillValue(9,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testRemaining1Cubes(self):
        solver = Remaining1()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(2,2,0)
        b.fillValue(8,2,0)
        b.fillValue(2,8,0)
        b.fillValue(8,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationRow(self):
        solver = Elimination()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationRowsCols(self):
        solver = Elimination()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        b.fillValue(1,2,0)
        b.fillValue(3,3,0)
        b.fillValue(4,4,0)
        b.fillValue(5,5,0)
        b.fillValue(1,8,0)
        b.fillValue(2,8,0)
        b.fillValue(3,8,0)
        b.fillValue(4,8,0)
        b.fillValue(7,8,0)
        b.fillValue(8,8,0)
        b.fillValue(9,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationCubes(self):
        solver = Elimination()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(2,2,0)
        b.fillValue(8,2,0)
        b.fillValue(2,8,0)
        b.fillValue(8,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationCubes(self):
        solver = Elimination()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        logging.debug(b.values())
        valuesFull = b.values()
        b.fillValue(2,2,0)
        b.fillValue(8,2,0)
        b.fillValue(2,8,0)
        b.fillValue(8,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationEasy(self):
        solver = Elimination()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.easy1)
        logging.debug(b.values())
        expected = examples.full1
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(expected,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationMedium(self):
        solver = Elimination()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.medium2)
        logging.debug(b.values())
        expected = examples.full2
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(expected,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testElimination2Row(self):
        solver = EliminationCouples()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testElimination2RowsCols(self):
        solver = EliminationCouples()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        b.fillValue(1,2,0)
        b.fillValue(3,3,0)
        b.fillValue(4,4,0)
        b.fillValue(5,5,0)
        b.fillValue(1,8,0)
        b.fillValue(2,8,0)
        b.fillValue(3,8,0)
        b.fillValue(4,8,0)
        b.fillValue(7,8,0)
        b.fillValue(8,8,0)
        b.fillValue(9,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testElimination2Cubes(self):
        solver = EliminationCouples()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(2,2,0)
        b.fillValue(8,2,0)
        b.fillValue(2,8,0)
        b.fillValue(8,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testElimination2Cubes(self):
        solver = EliminationCouples()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        logging.debug(b.values())
        valuesFull = b.values()
        b.fillValue(2,2,0)
        b.fillValue(8,2,0)
        b.fillValue(2,8,0)
        b.fillValue(8,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testElimination2Easy(self):
        solver = EliminationCouples()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.easy1)
        logging.debug(b.values())
        expected = examples.full1
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(expected,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testElimination2Medium(self):
        solver = EliminationCouples()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.medium2)
        logging.debug(b.values())
        expected = examples.full2
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(expected,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testPlacementRowsCols(self):
        solver = Placement()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        b.fillValue(1,2,0)
        b.fillValue(3,3,0)
        b.fillValue(4,4,0)
        b.fillValue(5,5,0)
        b.fillValue(1,8,0)
        b.fillValue(2,8,0)
        b.fillValue(3,8,0)
        b.fillValue(4,8,0)
        b.fillValue(7,8,0)
        b.fillValue(8,8,0)
        b.fillValue(9,8,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testPlacementMedium(self):
        solver = Placement()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.medium2)
        logging.debug(b.values())
        expected = examples.full2
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(expected,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve. Expected: {}'.format(steps, expected))

    def _testMultiMedium(self):
        solver = MultiSolver()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.medium2)
        logging.debug(b.values())
        expected = examples.full2
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(expected,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))
            logging.debug(expected)

    def _testMultiHard(self):
        solver = MultiSolver()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.hard3)
        logging.debug(b.values())
        expected = examples.full3
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(expected,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationRemainingRow(self):
        solver = EliminationRemaining()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        b.fillValue(9,2,0)
        b.fillValue(8,7,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))

    def _testEliminationRemainingMedium(self):
        solver = EliminationRemaining()
        examples = ExamplesDim9()
        b = Board(9)
        b.populate(examples.full1)
        valuesFull = b.values()
        b.fillValue(1,1,0)
        logging.debug(b.values())
        valuesBefore = b.values()
        steps = solver.solve(b)
        valuesAfter = b.values()
        logging.debug(b.values())
        if np.array_equal(valuesFull,valuesBefore):
            print('Setup error: did not remove values')
        if np.array_equal(valuesFull,valuesAfter):
            print('Pass: solver restored missing values in {} steps'.format(steps))
        else:
            print('Fail: solver performed {} steps and was not able to solve'.format(steps))


    def run(self):

        self._testRemaining1Row()
        self._testRemaining1RowsCols()
        self._testRemaining1Cubes()

        self._testEliminationRow()
        self._testEliminationRowsCols()
        self._testEliminationCubes()
        self._testEliminationEasy()
        self._testEliminationMedium()

        self._testElimination2Row()
        self._testElimination2RowsCols()
        self._testElimination2Cubes()
        self._testElimination2Easy()
        
        self._testEliminationRemainingRow()
        self._testEliminationRemainingMedium()

        self._testPlacementRowsCols()
        self._testPlacementMedium()

        self._testMultiMedium()
        self._testMultiHard()
        
logging.basicConfig(level=logging.WARN)

SolverTests().run()