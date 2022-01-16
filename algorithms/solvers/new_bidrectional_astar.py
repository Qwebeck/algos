from typing import Reversible
from algorithms.base.heuristic import Heuristic
from algorithms.base.problem import Problem, ReversibleProblem
from algorithms.base.solver import BidirectionalHeuristicSolver, HeuristicSolver
from algorithms.base.state import State
from algorithms.solvers.generic.bidirectional_search import BidirectionalSearch

from algorithms.tree.tree import Tree


class NBAstar(BidirectionalHeuristicSolver):
    def __init__(self, problem: ReversibleProblem,
                 primary_heuristic: Heuristic[State],
                 opposite_heuristic: Heuristic[State]):
        super().__init__(problem, primary_heuristic, opposite_heuristic)
        self.search = BidirectionalSearch(problem,
                                          primary_heuristic,
                                          opposite_heuristic)

    def solve(self):
        return self.search.solve()

    def search_tree(self) -> Tree:
        return self.search.search_tree
