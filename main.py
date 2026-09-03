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
    raise NotImplementedError

# def lrtastar_search(
#     problem: SearchProblem[StateT, ActionT],
#     h: Heuristic[StateT],
#     max_steps: int,
# ) -> SearchResult[ActionT] | None:
#     s, a = NULL, NULL  # Initialize state and action to null
#     result = SearchResult(actions=[], cost=0.0)  # Initialize result
#     H = {}  # Initialize heuristic dictionary
    
    
#     while (max_steps > 0):
#         # Return SearchResult if goal is reached
#         if (problem.is_goal(s)):
#             return result
        
#         # If s' is new, add it to the heuristic dictionary
#         if (s not in H):
#             s_prime = problem.result(s, a)
#             H[s_prime] = h(s_prime)
            
#         # If s is not null, find the best action and update the heuristic
#         if (s is not NULL):
#             # Add action taken to SearchResult
#             result.actions.append(a)
            
#             # Determine the next state s' and update the heuristic and result cost
#             s_prime = problem.result(s, a)
#             H[s] = min(H[s], result.cost + problem.action_cost(s, a, s_prime))
#             result.cost += problem.action_cost(s, a, s_prime)
            
            
#             # Determine the best action a' from s' and update the current state and action
#             a = min(
#                 problem.actions(s_prime),
#                 key=lambda a_prime: problem.action_cost(s_prime, a_prime, problem.result(s_prime, a_prime)) + H[problem.result(s_prime, a_prime)],
#             )
            
#             # Update the current state to the next state
#             s = s_prime

#         # Decrement max_steps and return None if the maximum number of steps is reached
#         max_steps -= 1
#         return None
    
            
            
            
            
    
    
    
    
    
#     """
#     Perform Learning Real-Time A* on the provided problem using the provided
#     heuristic function.

#     Args:
#         problem:
#             The search problem.

#         h:
#             The initial heuristic function.

#         max_steps:
#             Maximum number of actions that may be executed. This prevents
#             an unreachable goal or a nonconverging run from continuing
#             indefinitely.

#     Returns:
#         SearchResult if a goal state is reached.
#         None if max_steps is reached or a non-goal state has no actions.
#     """
    
def lrtastar_cost(problem, s, b, s_prime, H):
    if (s_prime is NULL):
        return lrtastar_heuristic(s)
    else:
        return problem.action_cost(s, b, s_prime) + H[s_prime]


def lrtastar_search(
    problem: SearchProblem[StateT, ActionT],
    h: Heuristic[StateT],
    max_steps: int,
) -> SearchResult[ActionT] | None:
    s, a = NULL, NULL  # Initialize state and action to null
    search_result = SearchResult(actions=[], cost=0.0)  # Initialize result
    results = {}  # Initialize results dictionary (s, a) -> s'
    H = {}  # Initialize heuristic dictionary
    
    while (max_steps > 0):
        s_prime = problem.result(s, a) if s is not NULL and a is not NULL else NULL
        
        # Check if current state is goal state
        if (problem.is_goal(s)):
            return search_result
        
        # Check if current state is in dictionary
        if (s not in H):
            H[s_prime] = h(s_prime)
            
        if (s is not NULL):
            # Add pair mapping of (s, a) to s' in results dictionary
            results[(s, a)] = s_prime
            H[s] = min(lrtastar_cost(problem, s, b, results[(s, b)], H), H)
            
        a = min(lrtastar_cost(problem, s, a, results[(s, a)], H), H)
        s = s_prime
            
    
            
            
    max_steps -= 1
            
    
    
    
    
    
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
    
