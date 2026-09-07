"""Student implementations for CS 4341 Assignment 1."""
from __future__ import annotations
import heapq

# Import utilities
try:
    from .search import (
        ActionT,
        Heuristic,
        SearchProblem,
        SearchResult,
        StateT,
    )
except ImportError:
    from search import (
        ActionT,
        Heuristic,
        SearchProblem,
        SearchResult,
        StateT,
    )

# ---------------------------------------------------------------------------
# A*
# ---------------------------------------------------------------------------

def astar_heuristic(state: StateT) -> float:
    """
    Estimate the remaining cost from state to a goal.
    """
    found = set()

    for row in range(5):
        for col in range(5):
            symbol = state[row][col]

            if symbol == " " or symbol == "*" or symbol in found:
                continue

            # Find matching rune.
            for newRow in range(row, 5):
                start_col = col + 1 if newRow == row else 0

                for newCol in range(start_col, 5):
                    if state[newRow][newCol] != symbol:
                        continue

                    found.add(symbol)

                    # Pair is in different rows AND columns.
                    if row != newRow and col != newCol:
                        return 2.0

                    # Pair is in the same row.
                    if row == newRow:
                        start = min(col, newCol)
                        end = max(col, newCol)

                        for c in range(start + 1, end):
                            if state[row][c] == "*":
                                return 3.0

                    # Pair is in the same column.
                    elif col == newCol:
                        start = min(row, newRow)
                        end = max(row, newRow)

                        for r in range(start + 1, end):
                            if state[r][col] == "*":
                                return 3.0

                    break
                else:
                    continue
                break

    # There are remaining pairs, and none requires more than
    # the cases above.
    return 1.0

def astar_search(
    problem: SearchProblem[StateT, ActionT],
    h: Heuristic[StateT],
) -> SearchResult[ActionT] | None:
    """
    Perform A* graph search on the provided problem using the provided
    heuristic function.

    Args:
        problem:
            The search problem.

        h:
            The heuristic function.

    Returns:
        SearchResult if a path to a goal state is found.
        None if there is no path to a goal state.
    """
    initialState=problem.initial
    currentActionCost = 0
    action = 0
    frontier = []
    heapq.heapify(frontier)

    while not problem.is_goal(StateT,StateT):
        for i in problem.actions:
                if h(problem.result(StateT,ActionT)) < frontier[0]:
                    frontier.heappush(h(problem.result(StateT,ActionT)))
                    action = i
        StateT = StateT.result(StateT, StateT, action)
        currentActionCost+=1

    raise NotImplementedError

# ---------------------------------------------------------------------------
# Learning Real-Time A*
# ---------------------------------------------------------------------------

def lrtastar_heuristic(state: StateT) -> float:
    """
    Estimate the remaining cost from state to a goal.
    """
    raise NotImplementedError

def lrtastar_search(
    problem: SearchProblem[StateT, ActionT],
    h: Heuristic[StateT],
    max_steps: int,
) -> SearchResult[ActionT] | None:
    """
    Perform Learning Real-Time A* on the provided problem using the provided
    heuristic function.

    Args:
        problem:
            The search problem.

        h:
            The initial heuristic function.

        max_steps:
            Maximum number of actions that may be executed. This prevents
            an unreachable goal or a nonconverging run from continuing
            indefinitely.

    Returns:
        SearchResult if a goal state is reached.
        None if max_steps is reached or a non-goal state has no actions.
    """
    

    raise NotImplementedError
