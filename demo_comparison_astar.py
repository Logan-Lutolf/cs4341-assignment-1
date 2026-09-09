from __future__ import annotations

import time
from collections import Counter
from runeshifter import RuneShifter, GameState
from search import SearchResult
from main import astar_search, astar_heuristic

DEMO_STATE: GameState = (
    ('e', 'e', 'f', 'f', 'l'),
    ('c', 'h', 'i', 'l', 'i'),
    ('c', 'a', ' ', 'h', 'b'),
    ('g', 'd', 'b', 'j', 'd'),
    ('a', 'k', 'k', 'g', 'j')
)

def uniform_cost_search(
    problem: SearchProblem[StateT, ActionT],
) -> SearchResult[ActionT] | None:
    """Uniform-cost graph search baseline."""

    import heap

    frontier = []
    tie_breaker = 0

    # (g_cost, insertion_order, state, actions)
    heapq.heappush(
        frontier,
        (0.0, tie_breaker, problem.initial, [])
    )

    best_cost = {
        problem.initial: 0.0
    }

    expanded = 0

    while frontier:
        cost, _, state, actions = heapq.heappop(frontier)

        # Ignore outdated entries.
        if cost > best_cost[state]:
            continue

        expanded += 1

        # Goal test.
        if problem.is_goal(state):
            return SearchResult(actions, expanded)

        # Expand actions in the order supplied by the problem.
        for action in problem.actions(state):
            next_state = problem.result(state, action)

            new_cost = (
                cost
                + problem.action_cost(state, action, next_state)
            )

            if next_state not in best_cost or new_cost < best_cost[next_state]:
                best_cost[next_state] = new_cost

                tie_breaker += 1

                heapq.heappush(
                    frontier,
                    (
                        new_cost,
                        tie_breaker,
                        next_state,
                        actions + [action],
                    ),
                )

    return None
