from typing import Optional
from algorithms.base.heuristic import Heuristic
from algorithms.base.solver import HeuristicSolver
from algorithms.solvers.generic.best_first import BestFirstSearch
from algorithms.tree.node import Node
from algorithms.tree.tree import Tree


class Greedy(HeuristicSolver):
    def __init__(self, problem, heuristic):
        super().__init__(problem, heuristic)
        self.search = BestFirstSearch(problem, lambda node: heuristic(node.state))

    def solve(self) -> Optional[Node]:
        return self.search.solve()

    def search_tree(self) -> Tree:
        return self.search.tree
