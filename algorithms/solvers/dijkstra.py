from typing import Optional
from algorithms.base.solver import Solver
from algorithms.solvers.generic.best_first import BestFirstSearch
from algorithms.tree.node import Node
from algorithms.tree.tree import Tree


class Dijkstra(Solver):
    def __init__(self, problem):
        super().__init__(problem)
        self.search = BestFirstSearch(problem, eval_fun=lambda node: node.cost)

    def solve(self) -> Optional[Node]:
        return self.search.solve()

    def search_tree(self) -> Tree:
        return self.search.tree
