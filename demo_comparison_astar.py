from __future__ import annotations

import time
from collections import Counter
from runeshifter import RuneShifter, GameState
from search import SearchProblem, SearchResult, StateT, ActionT
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

    import heapq

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

def print_state(state: GameState) -> None:

    print("+---+---+---+---+---+")

    for row in state:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+")


def replay_actions(
    problem,
    actions,
) -> tuple[GameState, float]:

    state = problem.initial
    total_cost = 0.0

    for action in actions:
        next_state = problem.result(state, action)
        total_cost += problem.action_cost(
            state,
            action,
            next_state,
        )
        state = next_state

    return state, total_cost


def analyze_repeated_states(
    problem,
    actions,
) -> tuple[int, int, list[tuple[int, GameState]]]:

    state = problem.initial
    states = [state]

    for action in actions:
        state = problem.result(state, action)
        states.append(state)

    counts = Counter(states)

    repeated_visits = sum(
        count - 1
        for count in counts.values()
        if count > 1
    )

    repeated_details = [
        (step, state)
        for step, state in enumerate(states)
        if counts[state] > 1
    ]

    return len(states), repeated_visits, repeated_details


def print_repeated_state_summary(
    problem,
    actions,
) -> None:

    total_states, repeated_visits, repeated_details = (
        analyze_repeated_states(problem, actions)
    )

    unique_states = total_states - repeated_visits

    print(f"  States encountered: {total_states}")
    print(f"  Unique states:      {unique_states}")
    print(f"  Repeated visits:    {repeated_visits}")

    if repeated_visits:
        state = problem.initial
        states = [state]
        for action in actions:
            state = problem.result(state, action)
            states.append(state)
        counts = Counter(states)
        repeated = [
            (state, count)
            for state, count in counts.items()
            if count > 1
        ]
        print(f"  States revisited:   {len(repeated)}")
        for index, (repeated_state, count) in enumerate(repeated[:3], 1):
            steps = [
                step
                for step, state_at_step in enumerate(states)
                if state_at_step == repeated_state
            ]
            print(
                f"    Example {index}: visited {count} times "
                f"at steps {steps}"
            )


def measure_runtime(
    search_function,
    problem,
    heuristic,
    max_steps=None,
    repetitions: int = 5,
):

    times = []
    results = []

    for _ in range(repetitions):
        fresh_problem = RuneShifter(initial=DEMO_STATE)
        start = time.perf_counter()
        if max_steps is None:
            result = search_function(
                fresh_problem,
                heuristic,
            )
        else:
            result = search_function(
                fresh_problem,
                heuristic,
                max_steps,
            )
        elapsed = time.perf_counter() - start
        times.append(elapsed)
        results.append(result)

    average = sum(times) / len(times)

    return average, results

def analyze_result(
    name: str,
    problem,
    result: SearchResult | None,
) -> None:

    print("=" * 70)
    print(name)
    print("=" * 70)

    if result is None:
        print("Result: FAILED TO REACH A GOAL")
        print()
        print(
            "The search returned None. Its implementation does not return "
            "the partial action sequence in this case, so path-level "
            "metrics cannot be independently computed from the result."
        )
        return

    final_state, path_cost = replay_actions(
        problem,
        result.actions,
    )

    correct = problem.is_goal(final_state)

    print(f"Solution found:    {correct}")
    print(f"Path length:       {len(result.actions)} actions")
    print(f"Path cost:         {path_cost:.1f}")
    print(f"Expanded/processed:{result.expanded}")
    print()

    print("Repeated-state behavior:")
    print_repeated_state_summary(
        problem,
        result.actions,
    )

    print()
    print("Action sequence:")
    print("  " + " -> ".join(result.actions))

    print()
    print("Final state:")
    print_state(final_state)

    print()
    print(f"Independent correctness check: {'PASS' if correct else 'FAIL'}")

def main() -> None:
    print()
    print("=" * 70)
    print("RUNE SHIFTER: UNIFORM COST SEARCH vs. A*")
    print("=" * 70)

    problem = RuneShifter(initial=DEMO_STATE)

    print("\nInitial demonstration state:")
    print_state(DEMO_STATE)

    print()
    print("Running both algorithms from the EXACT SAME initial state.")
    print("All Rune Shifter actions have cost 1.0.")
    print()

    ucs_problem = RuneShifter(initial=DEMO_STATE)
    ucs_start = time.perf_counter()
    ucs_result = uniform_cost_search(ucs_problem)
    ucs_time = time.perf_counter() - ucs_start

    astar_problem = RuneShifter(initial=DEMO_STATE)
    astar_start = time.perf_counter()
    astar_result = astar_search(astar_problem, astar_heuristic)
    astar_time = time.perf_counter() - astar_start

    print()
    analyze_result(
        "UNIFORM COST SEARCH",
        ucs_problem,
        ucs_result,
    )

    print()
    analyze_result(
        "A*",
        astar_problem,
        astar_result,
    )

    print()
    print("=" * 70)
    print("RUNNING TIME")
    print("=" * 70)

    print(f"Uniform Cost: {ucs_time * 1000:.3f} ms")
    print(f"A*:           {astar_time * 1000:.3f} ms")

    if ucs_time > 0:
        print(
            f"A* / Uniform Cost runtime ratio: "
            f"{astar_time / ucs_time:.2f}x"
        )

    print()
    print("=" * 70)
    print("COMPARISON SUMMARY")
    print("=" * 70)

    print(
        f"{'Metric':<25}"
        f"{'Uniform Cost':>18}"
        f"{'A*':>18}"
    )
    print("-" * 61)

    def metric_value(result, metric):
        if result is None:
            return "FAILED"

        if metric == "cost":
            _, cost = replay_actions(
                RuneShifter(initial=DEMO_STATE),
                result.actions,
            )
            return f"{cost:.1f}"

        if metric == "expanded":
            return str(result.expanded)

        if metric == "repeated":
            _, repeated, _ = analyze_repeated_states(
                RuneShifter(initial=DEMO_STATE),
                result.actions,
            )
            return str(repeated)

        if metric == "length":
            return str(len(result.actions))

        return "N/A"

    rows = [
        ("Path cost", "cost"),
        ("Path length", "length"),
        ("Expanded / processed", "expanded"),
        ("Repeated visits", "repeated"),
        ("Running time (ms)", "time"),
    ]

    for label, metric in rows:
        if metric == "time":
            ucs_value = f"{ucs_time * 1000:.3f}"
            astar_value = f"{astar_time * 1000:.3f}"
        else:
            ucs_value = metric_value(ucs_result, metric)
            astar_value = metric_value(astar_result, metric)

        print(
            f"{label:<25}"
            f"{ucs_value:>18}"
            f"{astar_value:>18}"
        )


if __name__ == "__main__":
    main()
