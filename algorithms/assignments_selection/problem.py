from dataclasses import astuple, dataclass
from enum import IntEnum
from typing import List
from algorithms.base import Problem
from algorithms.base.heuristic import Heuristic
from algorithms.base.state import State


class Estimation(IntEnum):
    Easy = 1
    Normal = 2
    Hard = 3


@dataclass
class Task:
    description: str
    max_points: int
    complexity: Estimation
    estimated_time: Estimation
    required_attention: Estimation
    required_creativity: Estimation

    def __hash__(self):
        return hash(astuple(self))

    def __lt__(self, other):
        return astuple(self) < astuple(other)

    def __eq__(self, other):
        return astuple(self) == astuple(other)

    def __gt__(self, other):
        return astuple(self) > astuple(other)


class TaskAssignment(State):
    def __init__(self, collected_points, assigned_tasks: List[Task]):
        self.collected_points = collected_points
        self.assigned_tasks = assigned_tasks

    def add_task(self, task: Task):
        return TaskAssignment(
            collected_points=self.collected_points + task.max_points,
            assigned_tasks=[*self.assigned_tasks, task]
        )

    def __hash__(self):
        return hash((self.collected_points, *[t for t in self.assigned_tasks]))


@dataclass
class TakeTask:
    task: Task
    assignment: TaskAssignment

    def cost(self):
        t = self.task
        return int(t.complexity) + int(t.estimated_time) + int(t.required_attention)

    def take(self) -> TaskAssignment:
        return self.assignment.add_task(self.task)


class TaskAssignmentProblem(Problem[TaskAssignment, TakeTask]):
    def __init__(self, available_tasks: List[Task], minimal_points: int):
        self._tasks = available_tasks
        self.min_points_count = minimal_points
        self.free_tasks = set(available_tasks)
        super().__init__(TaskAssignment(collected_points=0, assigned_tasks=[]))

    def take_action(self, assignment: TaskAssignment, action: TakeTask):
        return action.take()

    def action_cost(self, assignment: TaskAssignment, take_task: TakeTask):
        return take_task.cost()

    def is_goal(self, assignment: TaskAssignment) -> bool:
        return self.min_points_count == assignment.collected_points

    def actions(self, task_assignment: TaskAssignment):
        tasks = sorted(list(self.free_tasks - set(task_assignment.assigned_tasks)))
        return [TakeTask(task, task_assignment) for task in tasks]

    @staticmethod
    def deserialize():
        pass


class TaskAssignmentProblemHeuristic(Heuristic):

    def __init__(self, problem: TaskAssignmentProblem) -> None:
        """ creates a heuristic for the given problem
            this method should use to precalculate helper functions
        """
        self._problem = problem

    def __call__(self, state: TaskAssignment) -> float:
        """ calculates approximiate distance from the given state to the goal """
        return abs(state.collected_points - self._problem.min_points_count)
