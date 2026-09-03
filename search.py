"""Shared search interfaces for CS 4341 Assignment 1."""
from __future__ import annotations

# Import packages
from dataclasses import dataclass
from typing import (
    Callable,
    Generic,
    Hashable,
    Iterable,
    Protocol,
    TypeVar
)

# ---------------------------------------------------------------------------
# Type variables
# ---------------------------------------------------------------------------

StateT = TypeVar("StateT", bound=Hashable)
ActionT = TypeVar("ActionT", bound=Hashable)
Heuristic = Callable[[StateT], float]

# ---------------------------------------------------------------------------
# Search problem interface
# ---------------------------------------------------------------------------

class SearchProblem(Protocol[StateT, ActionT]):
    """
    Interface required by A* and LRTA*.

    States and actions must be hashable because the algorithms use them as
    dictionary keys.

    For deterministic grading, actions(state) returns actions in a
    deterministic order. Both algorithms should choose the first action or
    node encountered when priority values are equal.
    """

    initial: StateT

    def actions(self, state: StateT) -> Iterable[ActionT]:
        """Return the actions applicable in state."""
        ...

    def result(self, state: StateT, action: ActionT) -> StateT:
        """Return the state produced by applying action in state."""
        ...

    def action_cost(
        self,
        state: StateT,
        action: ActionT,
        next_state: StateT,
    ) -> float:
        """Return the one-step cost from state to next_state."""
        ...

    def is_goal(self, state: StateT) -> bool:
        """Return True exactly when state is a goal state."""
        ...

# ---------------------------------------------------------------------------
# Search result data class
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class SearchResult(Generic[ActionT]):
    """
    Result returned when a search reaches a goal.

    Attributes:
        actions:
            Actions in execution order from the initial state to a goal.

        expanded:
            For A*, the number of nodes expanded from the frontier,
            including the goal node.

            LRTA* has no frontier. For LRTA*, this is the number of states
            processed by the algorithm, including the initial state,
            repeated states, and the final goal state.
    """

    actions: list[ActionT]
    expanded: int
