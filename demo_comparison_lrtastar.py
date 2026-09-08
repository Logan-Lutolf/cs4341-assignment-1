from __future__ import annotations

import time
from collections import Counter
from runeshifter import RuneShifter, GameState
from search import SearchResult
from main import lrtastar_search, lrtastar_heuristic

DEMO_STATE: GameState = (
    (' ', 'b', 'j', 'i', 'f'),
    ('k', 'b', 'j', 'i', 'f'),
    ('k', 'c', 'd', 'h', 'e'),
    ('a', 'c', 'd', 'h', 'e'),
    ('a', 'l', 'l', 'g', 'g')
)

def greedy_local_search(
    problem,
    h,
    max_steps: int,
) -> SearchResult | None:

    state = problem.initial
    actions_taken = []
    expanded = 0

    for _ in range(max_steps):
        expanded += 1
        if problem.is_goal(state):
            return SearchResult(
                actions=actions_taken,
                expanded=expanded,
            )
        actions = list(problem.actions(state))
        if not actions:
            return None
        best_action = min(
            actions,
            key=lambda action: h(
                problem.result(state, action)
            ),
        )
        actions_taken.append(best_action)
        state = problem.result(state, best_action)

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
    print("RUNE SHIFTER: GREEDY SEARCH vs. LRTA*")
    print("=" * 70)

    problem = RuneShifter(initial=DEMO_STATE)

    print("\nInitial demonstration state:")
    print_state(DEMO_STATE)

    print()
    print("Running both algorithms from the EXACT SAME initial state.")
    print("All Rune Shifter actions have cost 1.0.")
    print()

    greedy_problem = RuneShifter(initial=DEMO_STATE)

    greedy_start = time.perf_counter()

    greedy_result = greedy_local_search(
        greedy_problem,
        lrtastar_heuristic,
        max_steps=10000,
    )

    greedy_time = time.perf_counter() - greedy_start

    lrta_problem = RuneShifter(initial=DEMO_STATE)

    lrta_start = time.perf_counter()

    lrta_result = lrtastar_search(
        lrta_problem,
        lrtastar_heuristic,
        max_steps=10000,
    )

    lrta_time = time.perf_counter() - lrta_start

    print()
    analyze_result(
        "GREEDY LOCAL SEARCH / HILL CLIMBING",
        greedy_problem,
        greedy_result,
    )

    print()
    analyze_result(
        "LRTA*",
        lrta_problem,
        lrta_result,
    )

    print()
    print("=" * 70)
    print("RUNNING TIME")
    print("=" * 70)

    print(f"Greedy: {greedy_time * 1000:.3f} ms")
    print(f"LRTA*:  {lrta_time * 1000:.3f} ms")

    if greedy_time > 0:
        print(
            f"LRTA* / Greedy runtime ratio: "
            f"{lrta_time / greedy_time:.2f}x"
        )

    print()
    print("=" * 70)
    print("COMPARISON SUMMARY")
    print("=" * 70)

    print(
        f"{'Metric':<25}"
        f"{'Greedy':>18}"
        f"{'LRTA*':>18}"
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
            greedy_value = f"{greedy_time * 1000:.3f}"
            lrta_value = f"{lrta_time * 1000:.3f}"
        else:
            greedy_value = metric_value(greedy_result, metric)
            lrta_value = metric_value(lrta_result, metric)

        print(
            f"{label:<25}"
            f"{greedy_value:>18}"
            f"{lrta_value:>18}"
        )

if __name__ == "__main__":
    main()
