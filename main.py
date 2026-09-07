"""Student implementations for CS 4341 Assignment 1."""
from __future__ import annotations
from asyncio.windows_events import NULL

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
    raise NotImplementedError

# ---------------------------------------------------------------------------
# Learning Real-Time A*
# ---------------------------------------------------------------------------

def lrtastar_heuristic(state: StateT) -> float:
    """
    Estimate the remaining cost from state to a goal.
    """
    positions: dict[str, list[tuple[int, int]]] = {}

    for i in range(5):
        for j in range(5):
            current = state[i][j]
            if current != " " and current != "*":
                positions.setdefault(current, []).append((i, j))

    score = 0.0

    for coordinates in positions.values():
        (row1, col1), (row2, col2) = coordinates
        score += 2.0
        score += abs(row1 - row2) + abs(col1 - col2)
        if row1 != row2 and col1 != col2:
            score += 2.0
        if row1 == row2:
            start = min(col1, col2)
            end = max(col1, col2)
            blockers = 0
            for col in range(start + 1, end):
                if state[row1][col] != " ":
                    blockers += 1
            score += 2.0 * blockers
        elif col1 == col2:
            start = min(row1, row2)
            end = max(row1, row2)
            blockers = 0
            for row in range(start + 1, end):
                if state[row][col1] != " ":
                    blockers += 1
            score += 2.0 * blockers

    return float(score)

def lrtastar_search(
    problem: SearchProblem[StateT, ActionT],
    h: Heuristic[StateT],
    max_steps: int,
) -> SearchResult[ActionT] | None:
    s, a = NULL, NULL  # Initialize state and action to null
    result = SearchResult(actions=[], cost=0.0)  # Initialize result
    H = {}  # Initialize heuristic dictionary


    while (max_steps > 0):
        # Return SearchResult if goal is reached
        if (problem.is_goal(s)):
            return result

        # If s' is new, add it to the heuristic dictionary
        if (s not in H):
            s_prime = problem.result(s, a)
            H[s_prime] = h(s_prime)

        # If s is not null, find the best action and update the heuristic
        if (s is not NULL):
            # Add action taken to SearchResult
            result.actions.append(a)

            # Determine the next state s' and update the heuristic and result cost
            s_prime = problem.result(s, a)
            H[s] = min(H[s], result.cost + problem.action_cost(s, a, s_prime))
            result.cost += problem.action_cost(s, a, s_prime)


            # Determine the best action a' from s' and update the current state and action
            a = min(
                problem.actions(s_prime),
                key=lambda a_prime: problem.action_cost(s_prime, a_prime, problem.result(s_prime, a_prime)) + H[problem.result(s_prime, a_prime)],
            )

            # Update the current state to the next state
            s = s_prime

        # Decrement max_steps and return None if the maximum number of steps is reached
        max_steps -= 1
        return None
    
            
            
            
            
    
    
    
    
    
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
    
