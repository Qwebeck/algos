from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar
from algorithms.base.state import State


S = TypeVar("S", bound=State)


@dataclass
class Node(Generic[S]):
    state: S
    parent: Optional[Node] = None
    action: Optional[object] = None
    cost: float = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self) -> str:
        return str(self.state)

    def __repr__(self) -> str:
        return f"<{str(self.parent)} --{self.action}--> {str(self.state)}. cost: {self.cost}>"

    def path(self) -> List['Node[S]']:
        node, path = self, []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]

    def reverse(self, zero_cost: float):
        def reverse_order(node):
            path = node.path()
            rpath = list(reversed(path))
            root = rpath[0]
            root.parent = None
            prev = root
            for n in rpath[1:]:
                n.parent = prev
                prev = n
            return rpath[-1]

        node = self
        old_prev_cost = node.cost
        node.cost = zero_cost
        prev_cost = node.cost
        while node.parent:
            node = node.parent
            cost = (old_prev_cost - node.cost) + prev_cost
            old_prev_cost = node.cost
            node.cost = cost
            prev_cost = cost

        return reverse_order(self)

    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()

    def has_cycle(self) -> bool:
        def find_cycle(ancestor):
            return ancestor is not None and (ancestor.state == self.state or find_cycle(ancestor.parent))
        return find_cycle(self.parent)
