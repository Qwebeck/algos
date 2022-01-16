from queue import Queue as FifoQueue
from algorithms.base.solver import P, Solver
from algorithms.solvers.generic.uninformed import UninformedSearch
from algorithms.solvers.utils import FIFO
from algorithms.tree import Node, Tree


class BFS(Solver):
    def __init__(self, problem: P):
        super().__init__(problem)
        self.search = UninformedSearch(problem, FIFO())

    def solve(self):
        return self.search.solve()

    def search_tree(self) -> Tree:
        return self.search.tree
