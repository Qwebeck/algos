from collections import deque
from typing import Deque
from algorithms.base.solver import P, Solver
from algorithms.solvers.generic.uninformed import UninformedSearch
from algorithms.solvers.utils import LIFO
from algorithms.tree import Node, Tree


class DFSIter(Solver):
    def __init__(self, problem: P):
        super().__init__(problem)
        self.search = UninformedSearch(problem, LIFO())

    def solve(self):
        return self.search.solve()

    def search_tree(self) -> Tree:
        return self.search.tree
