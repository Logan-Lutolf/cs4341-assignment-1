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

    # Create empty dictionary.
    positions = {}

    # For every row in the Rune Shifter board...
    for row_index, row in enumerate(state):

        # For every column in the Rune Shifter board...
        for column_index, cell in enumerate(row):

            # If the cell contains an unmerged rune...
            if cell not in (" ", "*"):

                # If this rune type has not yet been encountered...
                if cell not in positions:
                    positions[cell] = [] # Make room for the unpaired piece in the dictionary.

                # Store this rune's position in the dictionary.
                positions[cell].append((row_index, column_index))

    # If no pieces were found...
    if not positions:
        return 0.0 # Goal state has been reached and the heuristic is 0.

    # For every pair of runes in the grid...
    for pair_positions in positions.values():

        # Capture locations of both runes.
        first_position = pair_positions[0]
        second_position = pair_positions[1]

        # Compare row and column values between both runes.
        same_row = first_position[0] == second_position[0]
        same_column = first_position[1] == second_position[1]

        # If both runes share neither the same row nor column...
        if not same_row and not same_column:
            return 2.0 # Estimate that at least two moves are necessary to align both runes.

    # Otherwise, all remaining rune pairs share a row or a column.
    return 1.0 # Estimate that at least one move is necessarry to merge the remaining runes.

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

    import heapq

    # Preserve insertion order when priorities tie.
    tie_breaker = 0

    # For every frontier entry...
    # Store: (f_cost, insertion_order, state, g_cost, actions_taken)
    frontier = []

    # Start at problem's initial state.
    start_state = problem.initial

    # Cost from the start to itself is 0.
    start_cost = 0.0

    # A* priority:
    # f(n) = g(n) + h(n)
    start_priority = start_cost + h(start_state)

    # Add starting state to frontier.
    heapq.heappush(
        frontier,
        (start_priority, tie_breaker, start_state, start_cost, [])
    )

    # Store cheapest cost for reaching each state.
    best_cost = { start_state: 0.0 }

    # Number of nodes removed from frontier for processing.
    expanded = 0

    # While there are states left to explore...
    while frontier:

        # Remove state with the smallest f(n).
        priority, _, state, cost_so_far, actions_taken = heapq.heappop(frontier)

        # If this is an outdated, more expensive copy of a state...
        if cost_so_far > best_cost[state]:
            continue # Ignore state.

        # Next node now being processed.
        expanded += 1

        # If this state is the goal...
        if problem.is_goal(state):
            return SearchResult(actions_taken, expanded) # Return path used to reach state.

        # For every available action in the provided order...
        for action in problem.actions(state):

            # Find the state produced by taking this action.
            next_state = problem.result(state, action)

            # Find the total cost from start to next state.
            new_cost = (cost_so_far + problem.action_cost(state, action, next_state))

            # If state has never been seen or a cheaper way to reach it was found...
            if next_state not in best_cost or new_cost < best_cost[next_state]:

                # Record new cheapest cost.
                best_cost[next_state] = new_cost

                # Record action path used to reach current state.
                new_actions = actions_taken + [action]

                # A* priority = actual cost so far + estimated remaining cost.
                new_priority = new_cost + h(next_state)

                # Increase tie breaker so earlier nodes win ties.
                tie_breaker += 1

                # Add new state to frontier.
                heapq.heappush(
                    frontier,
                    (
                        new_priority,
                        tie_breaker,
                        next_state,
                        new_cost,
                        new_actions,
                    ),
                )

    # Frontier becomes empty without reaching a goal.
    return None

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
    

    raise NotImplementedError
