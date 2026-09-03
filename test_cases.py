"""Public tests for CS 4341 Assignment 1.

This file is generated. Do not edit it by hand.
"""

from __future__ import annotations

import pytest

try:
    from . import main
    from .runeshifter import Action, GameState, RuneShifter
    from .search import SearchResult
    from .test_heuristics import astar_heuristic, lrtastar_heuristic
except ImportError:
    import main
    from runeshifter import Action, GameState, RuneShifter
    from search import SearchResult
    from test_heuristics import astar_heuristic, lrtastar_heuristic


LRTASTAR_MAX_STEPS = 10000

INITIAL_STATES: tuple[GameState, ...] = (
    (('j', 'f', 'g', 'c', 'k'),
     ('l', 'f', 'e', 'd', 'e'),
     ('j', 'k', 'h', 'g', 'i'),
     ('b', 'l', 'b', 'h', 'a'),
     ('a', 'i', 'c', 'd', ' ')),
    (('f', 'b', 'a', 'l', ' '),
     ('e', 'g', 'd', 'j', 'g'),
     ('k', 'j', 'l', 'c', 'h'),
     ('d', 'c', 'h', 'a', 'b'),
     ('k', 'i', 'i', 'f', 'e')),
    (('j', ' ', 'f', 'g', 'g'),
     ('e', 'l', 'j', 'f', 'd'),
     ('c', 'i', 'e', 'b', 'h'),
     ('k', 'k', 'i', 'b', 'd'),
     ('h', 'l', 'a', 'a', 'c')),
    (('g', 'c', 'b', 'j', 'e'),
     ('h', 'g', 'd', 'h', 'l'),
     ('k', 'f', 'a', ' ', 'a'),
     ('j', 'e', 'b', 'f', 'i'),
     ('i', 'k', 'd', 'l', 'c')),
    (('j', 'l', 'c', 'i', 'c'),
     ('i', 'j', 'f', 'e', ' '),
     ('b', 'b', 'k', 'g', 'h'),
     ('k', 'f', 'd', 'h', 'e'),
     ('d', 'g', 'l', 'a', 'a')),
    (('h', 'i', ' ', 'd', 'f'),
     ('g', 'k', 'b', 'b', 'c'),
     ('l', 'e', 'g', 'j', 'h'),
     ('a', 'd', 'f', 'a', 'k'),
     ('i', 'c', 'l', 'e', 'j')),
    (('f', 'a', 'i', 'e', 'l'),
     ('k', 'b', ' ', 'j', 'c'),
     ('g', 'k', 'h', 'i', 'e'),
     ('l', 'j', 'f', 'd', 'c'),
     ('a', 'd', 'g', 'h', 'b')),
    (('d', 'k', 'f', 'a', 'g'),
     ('e', 'e', 'f', 'a', 'b'),
     ('i', 'b', 'l', 'g', 'k'),
     ('c', 'h', ' ', 'j', 'h'),
     ('i', 'c', 'd', 'j', 'l')),
    (('a', 'd', 'b', 'g', 'd'),
     (' ', 'k', 'l', 'i', 'k'),
     ('h', 'a', 'b', 'c', 'e'),
     ('i', 'c', 'j', 'f', 'l'),
     ('g', 'e', 'h', 'f', 'j')),
    ((' ', 'f', 'j', 'a', 'a'),
     ('k', 'd', 'f', 'g', 'i'),
     ('k', 'h', 'j', 'b', 'c'),
     ('g', 'e', 'i', 'h', 'b'),
     ('d', 'e', 'c', 'l', 'l')),
)

EXPECTED_ASTAR_RESULTS: tuple[
    SearchResult[Action] | None, ...
] = (
    SearchResult(
        actions=['right', 'down', 'left', 'up', 'right', 'down', 'up', 'left', 'down',
             'left', 'up', 'right', 'down', 'right', 'up', 'left', 'down', 'up',
             'right', 'down', 'up', 'left'],
        expanded=5129,
    ),
    SearchResult(
        actions=['right', 'down', 'left', 'up', 'right', 'up', 'down', 'right', 'up',
             'left', 'right', 'up', 'right', 'up', 'left', 'up', 'right', 'down',
             'left', 'down', 'right', 'up', 'down', 'left', 'up', 'right', 'down',
             'up', 'left', 'up', 'right', 'left', 'up', 'left'],
        expanded=4939,
    ),
    SearchResult(
        actions=['right', 'up', 'left', 'down', 'left', 'up', 'right', 'up', 'left',
             'down', 'left', 'up', 'right', 'up', 'right', 'left', 'up', 'right',
             'up'],
        expanded=224,
    ),
    SearchResult(
        actions=['right', 'up', 'left', 'down', 'right', 'up', 'left', 'up', 'down',
             'left', 'down', 'right', 'up', 'right', 'up', 'left', 'up', 'right',
             'down', 'left', 'up', 'right', 'up'],
        expanded=2568,
    ),
    SearchResult(
        actions=['left', 'up', 'right', 'left', 'down', 'right', 'up', 'left', 'up',
             'right', 'up', 'down', 'left', 'right', 'down', 'left', 'up', 'right',
             'up', 'right', 'up'],
        expanded=311,
    ),
    SearchResult(
        actions=['left', 'up', 'right', 'left', 'down', 'right', 'down', 'left', 'up',
             'down', 'right', 'up', 'left', 'up', 'right', 'up', 'left', 'down',
             'right', 'up', 'down', 'left', 'up', 'left', 'down', 'left', 'right',
             'up', 'left'],
        expanded=7517,
    ),
    SearchResult(
        actions=['right', 'up', 'down', 'left', 'down', 'right', 'up', 'left', 'down',
             'right', 'up', 'down', 'left', 'up', 'left', 'down', 'up', 'right',
             'down', 'left', 'up', 'right', 'up', 'right', 'left', 'down', 'left',
             'up', 'right', 'up', 'left'],
        expanded=6441,
    ),
    SearchResult(
        actions=['up', 'left', 'right', 'up', 'left', 'down', 'right', 'up', 'left',
             'up', 'left', 'down', 'right', 'down', 'left', 'up', 'left', 'up',
             'left', 'up'],
        expanded=4272,
    ),
    SearchResult(
        actions=['down', 'left', 'up', 'right', 'up', 'down', 'left', 'up', 'right',
             'left', 'down', 'left', 'up', 'right', 'up', 'left', 'up', 'left',
             'up', 'right', 'down', 'left', 'up', 'right', 'up', 'left', 'down',
             'left', 'right', 'up', 'right', 'up', 'left'],
        expanded=1438,
    ),
    SearchResult(
        actions=['up', 'right', 'up', 'left', 'up', 'right', 'up', 'left', 'up', 'down',
             'left', 'up', 'right', 'up', 'left', 'up', 'right', 'down', 'left',
             'right', 'up', 'right', 'up'],
        expanded=2194,
    ),
)

EXPECTED_LRTASTAR_RESULTS: tuple[
    SearchResult[Action] | None, ...
] = (
    SearchResult(
        actions=['up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right',
             'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'left', 'right', 'up', 'down', 'up', 'left', 'right', 'right',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up',
             'down', 'up', 'left', 'right', 'up', 'down', 'up', 'left', 'right',
             'right', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'up', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up', 'left',
             'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'down', 'left', 'up', 'up',
             'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up',
             'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'down', 'left', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right', 'right',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right',
             'right', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up',
             'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up',
             'down', 'up', 'up', 'up', 'down', 'down', 'left', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left'],
        expanded=657,
    ),
    None,
    SearchResult(
        actions=['up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up',
             'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down',
             'up', 'left', 'right', 'up', 'down', 'up', 'up', 'up', 'down', 'up',
             'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down',
             'up', 'left', 'up', 'down', 'down', 'left', 'right', 'up'],
        expanded=226,
    ),
    None,
    SearchResult(
        actions=['up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'down', 'left', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right', 'up',
             'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up',
             'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up',
             'down', 'up', 'left', 'right', 'up', 'down', 'up', 'left', 'right',
             'right', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'down', 'left', 'up',
             'up', 'down', 'up', 'left', 'right', 'up', 'right', 'up', 'left',
             'down', 'left', 'up', 'right', 'down', 'up', 'up', 'up', 'down', 'up',
             'up', 'up', 'down', 'down', 'left', 'up', 'right', 'left', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'right', 'down', 'left', 'down', 'up', 'up', 'left',
             'up', 'down', 'left', 'up', 'right', 'down', 'up', 'up', 'up', 'down',
             'up', 'up', 'up', 'down', 'down', 'left', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left'],
        expanded=327,
    ),
    None,
    SearchResult(
        actions=['up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right',
             'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'left', 'right', 'right', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'right',
             'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'down', 'left', 'up', 'up',
             'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left', 'right',
             'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up',
             'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up',
             'left', 'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'down', 'left', 'up', 'up', 'down',
             'up', 'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up',
             'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up',
             'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up', 'up',
             'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down',
             'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'down', 'up', 'left', 'right', 'up', 'down', 'up', 'up', 'up', 'down',
             'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down', 'down', 'left',
             'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up',
             'left', 'right', 'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up',
             'up', 'down', 'up', 'up', 'up', 'down', 'down', 'left', 'up', 'up',
             'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left', 'right',
             'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down', 'up',
             'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up',
             'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up',
             'up', 'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down',
             'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'down', 'up', 'left', 'right', 'up', 'down', 'up', 'up', 'up', 'down',
             'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down', 'down', 'left',
             'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right', 'right',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up',
             'up', 'down', 'up', 'left', 'up', 'down', 'down', 'left', 'up', 'up',
             'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up',
             'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'right', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'up',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'down',
             'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'left', 'right', 'right', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'down', 'left', 'up', 'up', 'down',
             'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'up', 'left', 'right', 'right', 'up', 'down', 'up', 'left', 'up',
             'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up',
             'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'up',
             'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left', 'right',
             'up', 'up', 'left', 'up', 'down', 'left', 'up', 'right', 'down', 'up',
             'up', 'left', 'up', 'down', 'left', 'up', 'right', 'down', 'up', 'up',
             'left', 'up', 'down', 'left', 'up', 'right', 'down', 'up', 'up',
             'left', 'up', 'down', 'left', 'up', 'right', 'down', 'up', 'up',
             'left', 'up', 'down', 'left', 'up', 'right', 'down', 'up', 'up',
             'left', 'up', 'down', 'left', 'up', 'right', 'down', 'up', 'up',
             'left', 'down', 'down', 'left', 'up', 'up', 'right', 'left', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'right', 'left',
             'up', 'down', 'up', 'up', 'right', 'right', 'up', 'up', 'down', 'up',
             'left', 'down', 'down', 'left', 'up', 'up', 'right', 'left', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'right', 'left',
             'up', 'down', 'up', 'up', 'right', 'right', 'up', 'up', 'down', 'up',
             'left', 'down', 'down', 'left', 'up', 'up', 'right', 'left', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'right', 'left',
             'up', 'down', 'up', 'up', 'right', 'right', 'up', 'up', 'down', 'up',
             'left', 'down', 'down', 'left', 'up', 'up', 'right', 'left', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'right', 'left',
             'up', 'down', 'up', 'up', 'right', 'right', 'up', 'up', 'down', 'up',
             'left', 'down', 'down', 'left', 'up', 'up', 'right', 'left', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'right', 'left',
             'up', 'down', 'up', 'up', 'right', 'right', 'up', 'up', 'down', 'up',
             'left', 'down', 'down', 'left', 'up', 'right', 'left', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'right', 'left',
             'up', 'down', 'up', 'up', 'right', 'right', 'left', 'up', 'down', 'up',
             'up', 'right', 'up', 'left', 'up', 'down', 'left', 'down', 'up', 'up',
             'up', 'down', 'up', 'right', 'up', 'left', 'up', 'down', 'left',
             'down', 'up', 'up', 'up', 'down', 'up', 'right', 'up', 'left', 'up',
             'down', 'left', 'down', 'up', 'up', 'up', 'down', 'up', 'right', 'up',
             'left', 'up', 'down', 'left', 'down', 'up', 'up', 'up', 'down', 'up',
             'right', 'up', 'left', 'up', 'down', 'left', 'down', 'up', 'up', 'up',
             'down', 'up', 'right', 'up', 'left', 'up', 'down', 'left', 'down',
             'up', 'up', 'right', 'up', 'up', 'left', 'down', 'down', 'up', 'up',
             'up', 'down', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'left', 'down', 'down', 'up', 'up', 'up', 'down', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'up', 'left', 'down', 'down', 'up', 'up',
             'up', 'down', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'left', 'down', 'down', 'up', 'up', 'up', 'down', 'right', 'up', 'up',
             'down', 'up', 'left', 'up', 'up', 'left', 'down', 'down', 'up', 'up',
             'up', 'down', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'left', 'down', 'down', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'up', 'left', 'up', 'down', 'left', 'left', 'right', 'up',
             'right', 'left', 'down', 'up', 'up', 'left', 'up', 'down', 'left',
             'left', 'right', 'up', 'right', 'left', 'down', 'up', 'up', 'left',
             'up', 'down', 'left', 'left', 'right', 'up', 'right', 'left', 'down',
             'up', 'up', 'left', 'up', 'down', 'left', 'left', 'right', 'up',
             'right', 'left', 'down', 'up', 'up', 'left', 'up', 'down', 'left',
             'left', 'right', 'up', 'right', 'left', 'down', 'up', 'left', 'up',
             'up', 'down', 'left', 'left', 'right', 'up', 'right', 'left', 'down',
             'up', 'up', 'left', 'down', 'right', 'down', 'up', 'left', 'left',
             'right', 'up', 'left', 'left', 'left', 'right', 'up', 'down', 'up',
             'up', 'left', 'up', 'up', 'down', 'up', 'left', 'down', 'right',
             'down', 'up', 'left', 'left', 'right', 'up', 'left', 'left', 'left',
             'right', 'up', 'down', 'up', 'up', 'left', 'up', 'up', 'down', 'up',
             'left', 'down', 'right', 'down', 'up', 'left', 'left', 'right', 'up',
             'left', 'left', 'left', 'right', 'up', 'down', 'up', 'up', 'left',
             'up', 'up', 'down', 'up', 'left', 'down', 'right', 'down', 'up',
             'left', 'left', 'right', 'up', 'left', 'left', 'left', 'right', 'up',
             'down', 'up', 'up', 'left', 'up', 'up', 'down', 'up', 'left', 'down',
             'right', 'down', 'up', 'left', 'left', 'right', 'up', 'left', 'left',
             'up', 'up', 'up', 'down', 'up', 'left', 'down', 'right', 'down', 'up',
             'left', 'left', 'right', 'up', 'left', 'left', 'left', 'right', 'up',
             'down', 'up', 'up', 'left', 'left', 'up', 'left', 'down', 'right',
             'left', 'right', 'right', 'left', 'left', 'left', 'right', 'right',
             'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up',
             'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up',
             'up', 'up', 'down', 'up', 'up', 'up', 'down', 'down', 'left', 'up',
             'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up',
             'left', 'up', 'down', 'down', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up',
             'left', 'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up',
             'down', 'down', 'left', 'right', 'up', 'right', 'left', 'down', 'up',
             'up', 'up', 'down', 'up', 'right', 'up', 'down', 'right', 'down', 'up',
             'left', 'left', 'right', 'up', 'left', 'left', 'up', 'up', 'right',
             'up', 'down', 'right', 'left', 'right', 'right', 'up', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'up', 'right', 'down', 'right', 'left', 'up', 'right', 'up', 'up',
             'down', 'left', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'left',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up',
             'right', 'down', 'down', 'up', 'up', 'up', 'down', 'down', 'right',
             'down', 'left', 'left', 'right', 'down', 'left', 'left', 'left',
             'right', 'up', 'up', 'left', 'up', 'up', 'up', 'down', 'down', 'left',
             'up', 'up', 'down', 'left', 'right', 'up'],
        expanded=1718,
    ),
    None,
    SearchResult(
        actions=['up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down',
             'up', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down',
             'up', 'left', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down',
             'left', 'up', 'right', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'down', 'down', 'left', 'up', 'right', 'down', 'up', 'up', 'up',
             'down', 'up', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'left',
             'up', 'right', 'left', 'right', 'right', 'left', 'up', 'down', 'up',
             'up', 'right', 'right', 'left', 'up', 'down', 'up', 'up', 'right',
             'up', 'up', 'left', 'down', 'left', 'down', 'up', 'up', 'right', 'up',
             'left', 'down', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up',
             'down', 'up', 'left', 'up', 'down', 'up', 'left', 'right', 'up',
             'down', 'up', 'left', 'right', 'right', 'up', 'down', 'up', 'left',
             'up', 'down', 'up', 'up', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'left', 'up',
             'right', 'up', 'right', 'up', 'up', 'down', 'up', 'left', 'down',
             'down', 'left', 'up', 'right', 'down', 'up', 'up', 'up', 'down', 'up',
             'up', 'up', 'down', 'up', 'left', 'up', 'down', 'left', 'up', 'right',
             'left', 'right', 'right', 'left', 'up', 'down', 'up', 'up', 'right',
             'right', 'left', 'up', 'down', 'up', 'up', 'right', 'up', 'up', 'left',
             'down', 'left', 'down', 'up', 'up', 'right', 'up', 'left', 'down',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down', 'up',
             'left', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up', 'up',
             'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up',
             'left', 'right', 'up', 'up', 'down', 'up', 'left', 'up', 'up', 'down',
             'up', 'left', 'right', 'up', 'down', 'up', 'up', 'up', 'down', 'up',
             'up', 'up', 'down', 'up', 'up', 'up', 'down', 'down', 'left', 'up',
             'up', 'down', 'up', 'left', 'right', 'up', 'up', 'down', 'up', 'left',
             'up', 'up', 'down', 'up', 'left', 'right', 'up', 'down', 'up', 'up',
             'up', 'down', 'up', 'up', 'up', 'down', 'up', 'up', 'up', 'down', 'up',
             'up', 'up', 'down', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'left', 'up', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'up', 'down', 'up', 'left', 'up', 'down', 'up', 'left',
             'right', 'up', 'down', 'up', 'left', 'right', 'right', 'up', 'down',
             'down', 'left', 'up', 'up', 'down', 'up', 'left', 'right', 'up', 'up',
             'down', 'up', 'left'],
        expanded=383,
    ),
    None,
)


class _DeadEndProblem:
    initial = "start"

    def actions(self, state: str) -> tuple[str, ...]:
        return ()

    def result(self, state: str, action: str) -> str:
        raise AssertionError("A dead-end state has no applicable actions.")

    def action_cost(
        self,
        state: str,
        action: str,
        next_state: str,
    ) -> float:
        raise AssertionError("A dead-end state has no action costs.")

    def is_goal(self, state: str) -> bool:
        return False


@pytest.mark.parametrize(
    "case_index",
    range(len(INITIAL_STATES)),
    ids=lambda index: f"case_{index + 1}",
)
def test_astar_search(case_index: int) -> None:
    actual = main.astar_search(
        RuneShifter(INITIAL_STATES[case_index]),
        astar_heuristic,
    )
    expected = EXPECTED_ASTAR_RESULTS[case_index]

    assert actual == expected, (
        f"A* public case {case_index + 1} failed: "
        f"expected {expected!r}, got {actual!r}"
    )


@pytest.mark.parametrize(
    "case_index",
    range(len(INITIAL_STATES)),
    ids=lambda index: f"case_{index + 1}",
)
def test_lrtastar_search(case_index: int) -> None:
    actual = main.lrtastar_search(
        RuneShifter(INITIAL_STATES[case_index]),
        lrtastar_heuristic,
        LRTASTAR_MAX_STEPS,
    )
    expected = EXPECTED_LRTASTAR_RESULTS[case_index]

    assert actual == expected, (
        f"LRTA* public case {case_index + 1} failed: "
        f"expected {expected!r}, got {actual!r}"
    )


def test_astar_returns_none_for_unreachable_problem() -> None:
    actual = main.astar_search(
        _DeadEndProblem(),
        lambda state: 0.0,
    )

    assert actual is None, (
        "A* must return None when no path to a goal exists; "
        f"got {actual!r}"
    )


def test_lrtastar_returns_none_for_dead_end() -> None:
    actual = main.lrtastar_search(
        _DeadEndProblem(),
        lambda state: 0.0,
        LRTASTAR_MAX_STEPS,
    )

    assert actual is None, (
        "LRTA* must return None when a non-goal state has no actions; "
        f"got {actual!r}"
    )


@pytest.mark.parametrize(
    ("heuristic_name", "heuristic"),
    (
        ("A*", main.astar_heuristic),
        ("LRTA*", main.lrtastar_heuristic),
    ),
)
def test_student_heuristic_returns_float(
    heuristic_name: str,
    heuristic: object,
) -> None:
    state = INITIAL_STATES[0]

    try:
        value = heuristic(state)
    except Exception as error:
        pytest.fail(
            f"{heuristic_name} heuristic raised "
            f"{type(error).__name__}: {error}"
        )

    assert type(value) is float, (
        f"{heuristic_name} heuristic must return a Python float; "
        f"got {type(value).__name__}"
    )
