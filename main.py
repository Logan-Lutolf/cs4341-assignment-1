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
    totalDistance = 0
    for row in range(5):
        for col in range(5):
            symbol = state[row][col]
            if symbol == " " or symbol == "*" or symbol in found:
                continue
            else:
                matchFound = False
                for newRow in range(row, 5):
                    if newRow == row:
                        start_col = col + 1 
                    else:
                        start_col = 0
                    for newCol in range(start_col, 5):
                        if state[newRow][newCol] == symbol:
                            found.add(symbol)
                            distance = abs(newRow-row) + abs(newCol-col)
                            print(distance)
                            totalDistance+=distance
                            matchFound = True
                            break
                        else:
                            continue
                    if matchFound == True:
                        break

    return float(totalDistance)
    raise NotImplementedError

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
