"""Reference heuristics used by the public tests."""
from __future__ import annotations

# Import utilities
try:
    from .runeshifter import EMPTY, GameState
except ImportError:
    from runeshifter import EMPTY, GameState

# Define heuristics
def _row_index_sum(state: GameState) -> float:
    return float(
        sum(
            row_index
            for row_index, row in enumerate(state)
            for cell in row
            if cell != EMPTY
        )
    )

def astar_heuristic(state: GameState) -> float:
    return _row_index_sum(state)

def lrtastar_heuristic(state: GameState) -> float:
    return _row_index_sum(state)
