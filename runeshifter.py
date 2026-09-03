"""Rune Shifter problem definition and optional terminal interface."""
from __future__ import annotations

# Import packages
import curses
import locale
import random
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Literal

# =============================================================================
# Rune Shifter Search Problem
# =============================================================================

# Define constants
GRID_SIZE = 5
N_PAIRS = 12
EMPTY = " "
MATCHED = "*"

# Define actions
Action = Literal["up", "down", "left", "right"]
ACTIONS: tuple[Action, ...] = (
    "up",
    "down",
    "left",
    "right",
)

# Define states
GameState = tuple[tuple[str, ...], ...]

# Define SearchProblem class
@dataclass(frozen=True)
class RuneShifter:

    initial: GameState

    def __post_init__(self) -> None:
        _validate_state(self.initial)

    @classmethod
    def random(cls, seed: int | None = None) -> RuneShifter:
        rng = random.Random(seed)

        markers = [
            chr(ord("a") + i)
            for i in range(N_PAIRS)
        ] * 2

        positions = [
            (row, column)
            for row in range(GRID_SIZE)
            for column in range(GRID_SIZE)
        ]

        selected_positions = rng.sample(
            positions,
            N_PAIRS * 2,
        )

        grid = [
            [EMPTY for _ in range(GRID_SIZE)]
            for _ in range(GRID_SIZE)
        ]

        for marker, (row, column) in zip(
            markers,
            selected_positions,
        ):
            grid[row][column] = marker

        return cls(initial=_freeze_grid(grid))

    def actions(self, state: GameState) -> Iterable[Action]:
        _validate_state(state)
        return ACTIONS

    def result(
        self,
        state: GameState,
        action: Action,
    ) -> GameState:
        _validate_state(state)

        if action not in ACTIONS:
            raise ValueError(f"Invalid action: {action!r}")

        grid = [
            list(row)
            for row in state
        ]

        for i in range(GRID_SIZE):
            positions = _positions_for_line(i, action)

            line = [
                grid[row][column]
                for row, column in positions
            ]

            _shift(line)

            for value, (row, column) in zip(line, positions):
                grid[row][column] = value

        return _freeze_grid(grid)

    def action_cost(
        self,
        state: GameState,
        action: Action,
        next_state: GameState,
    ) -> float:
        return 1.0

    def is_goal(self, state: GameState) -> bool:
        _validate_state(state)

        return all(
            cell in (EMPTY, MATCHED)
            for row in state
            for cell in row
        )

# Define helper functions
def _validate_state(state: GameState) -> None:
        if len(state) != GRID_SIZE:
            raise ValueError(
                f"State must have exactly {GRID_SIZE} rows."
            )

        for row in state:
            if len(row) != GRID_SIZE:
                raise ValueError(
                    f"Each row must have exactly {GRID_SIZE} cells."
                )

def _positions_for_line(
    index: int,
    action: Action,
) -> list[tuple[int, int]]:
    if action == "up":
        return [
            (row, index)
            for row in range(GRID_SIZE)
        ]

    if action == "down":
        return [
            (row, index)
            for row in range(GRID_SIZE - 1, -1, -1)
        ]

    if action == "left":
        return [
            (index, column)
            for column in range(GRID_SIZE)
        ]

    if action == "right":
        return [
            (index, column)
            for column in range(GRID_SIZE - 1, -1, -1)
        ]

    raise ValueError(f"Invalid action: {action!r}")

def _shift(line: list[str]) -> None:
    stop = 0

    for i in range(1, len(line)):
        if line[i] == EMPTY:
            continue

        if line[i] == MATCHED:
            stop = i

        elif line[stop] == EMPTY:
            line[stop] = line[i]
            line[i] = EMPTY

        elif line[i] == line[stop]:
            line[stop] = MATCHED
            line[i] = EMPTY
            stop += 1

        else:
            line[stop + 1] = line[i]

            if stop + 1 != i:
                line[i] = EMPTY

            stop += 1

def _freeze_grid(grid: list[list[str]]) -> GameState:
    return tuple(
        tuple(row)
        for row in grid
    )

# =============================================================================
# Terminal user interface
# =============================================================================

def safe_addstr(
    stdscr: curses.window,
    y: int,
    x: int,
    text: str,
    attributes: int = 0,
) -> None:
    height, width = stdscr.getmaxyx()

    if y < 0 or y >= height or x >= width:
        return

    if x < 0:
        text = text[-x:]
        x = 0

    available_width = width - x

    if available_width <= 0:
        return

    try:
        stdscr.addnstr(
            y,
            x,
            text,
            available_width,
            attributes,
        )
    except curses.error:
        pass

def draw(
    stdscr: curses.window,
    state: GameState,
    message: str = "",
) -> bool:
    stdscr.erase()

    cell_width = 3

    horizontal = (
        "+"
        + "+".join(["-" * cell_width] * GRID_SIZE)
        + "+"
    )

    controls = "Arrow keys: move | q or ESC: quit"

    required_width = max(
        len(horizontal),
        len(controls),
    )

    required_height = GRID_SIZE * 2 + 4

    height, width = stdscr.getmaxyx()

    if height < required_height or width < required_width:
        safe_addstr(
            stdscr,
            0,
            0,
            "Terminal window is too small.",
            curses.A_BOLD,
        )

        safe_addstr(
            stdscr,
            1,
            0,
            (
                f"Resize to at least {required_width} columns "
                f"by {required_height} rows."
            ),
        )

        safe_addstr(
            stdscr,
            2,
            0,
            "Press q or ESC to quit.",
        )

        stdscr.refresh()
        return False

    start_x = max(
        0,
        (width - len(horizontal)) // 2,
    )

    y = 0

    safe_addstr(stdscr, y, start_x, horizontal)
    y += 1

    for row in state:
        rendered_row = (
            "|"
            + "|".join(f" {cell} " for cell in row)
            + "|"
        )

        safe_addstr(
            stdscr,
            y,
            start_x,
            rendered_row,
        )
        y += 1

        safe_addstr(
            stdscr,
            y,
            start_x,
            horizontal,
        )
        y += 1

    y += 1

    controls_x = max(
        0,
        (width - len(controls)) // 2,
    )

    safe_addstr(
        stdscr,
        y,
        controls_x,
        controls,
    )

    if message:
        y += 1

        message_x = max(
            0,
            (width - len(message)) // 2,
        )

        safe_addstr(
            stdscr,
            y,
            message_x,
            message,
            curses.A_BOLD,
        )

    stdscr.refresh()
    return True

def main(stdscr: curses.window) -> None:
    stdscr.keypad(True)
    stdscr.timeout(-1)

    try:
        curses.curs_set(0)
    except curses.error:
        pass

    problem = RuneShifter.random()
    state = problem.initial

    key_to_action: dict[int, Action] = {
        curses.KEY_UP: "up",
        curses.KEY_DOWN: "down",
        curses.KEY_LEFT: "left",
        curses.KEY_RIGHT: "right",
    }

    while True:
        if problem.is_goal(state):
            draw(
                stdscr,
                state,
                "Winner - press any key to exit",
            )
            stdscr.getch()
            return

        screen_is_large_enough = draw(
            stdscr,
            state,
        )

        key = stdscr.getch()

        if key in (27, ord("q"), ord("Q")):
            return

        if key == curses.KEY_RESIZE:
            continue

        if not screen_is_large_enough:
            continue

        action = key_to_action.get(key)

        if action is not None:
            state = problem.result(state, action)

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "")
    curses.wrapper(main)
