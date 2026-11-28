"""Solutions for the ACME Standard Library lab.

Run ``python standard_library.py NAME SECONDS`` to play Shut the Box.
"""

import random
import sys
import time
from itertools import chain, combinations

import box
import calculator


def min_max_avg(values):
    """Return the minimum, maximum, and average of a nonempty list."""
    return min(values), max(values), sum(values) / len(values)


def hypotenuse(a, b):
    """Compute a right triangle's hypotenuse using only calculator functions."""
    return calculator.sqrt(calculator.sum(calculator.product(a, a), calculator.product(b, b)))


def power_set(values):
    """Return every subset of the input iterable as a set."""
    entries = tuple(values)
    return [set(group) for group in chain.from_iterable(
        combinations(entries, count) for count in range(len(entries) + 1)
    )]


def play_game(name, time_limit, input_fn=input, randint=random.randint, clock=time.monotonic):
    """Play one timed game; optional callables make the rules testable."""
    remaining = list(range(1, 10))
    start = clock()
    while remaining:
        seconds_left = time_limit - (clock() - start)
        if seconds_left <= 0:
            print("Time is up!")
            break

        roll = randint(1, 6)
        if sum(remaining) > 6:
            roll += randint(1, 6)
        if not box.isvalid(roll, remaining):
            print(f"No combination can match the roll of {roll}.")
            break

        print("Numbers left:", remaining)
        print("Roll:", roll)
        print("Seconds left:", round(seconds_left, 2))
        while True:
            if clock() - start >= time_limit:
                print("Time is up!")
                break
            answer = input_fn("Numbers to eliminate: ")
            if clock() - start >= time_limit:
                print("Time is up!")
                break
            choices = box.parse_input(answer, remaining)
            if choices and sum(choices) == roll:
                for choice in choices:
                    remaining.remove(choice)
                break
            print("Invalid choice; try again.")
        if clock() - start >= time_limit:
            break

    won = not remaining
    elapsed = clock() - start
    print(f"Score for player {name}: {sum(remaining)} points")
    print(f"Time played: {elapsed:.2f} seconds")
    print("Congratulations! You shut the box!" if won else "Better luck next time!")
    return won, sum(remaining)


if __name__ == "__main__" and len(sys.argv) == 3:
    try:
        limit = float(sys.argv[2])
        if limit > 0:
            play_game(sys.argv[1], limit)
    except ValueError:
        pass
