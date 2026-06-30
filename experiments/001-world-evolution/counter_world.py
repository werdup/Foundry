"""
Experiment 001A

Question
--------
Who has authority over objective state?

This experiment intentionally avoids using Foundry abstractions.
The objective is to understand the smallest possible world before
attempting to generalize it.

Expected outcome:
The experiment should produce architectural observations rather than
reusable code.
"""


class CounterWorld:
    """The smallest possible world."""

    def __init__(self):
        # Objective state.
        self.counter = 0


def main():

    world = CounterWorld()

    print(f"Initial counter: {world.counter}")

    #
    # The experiment exercises authority over objective state directly.
    #
    world.counter += 1

    print(f"Updated counter: {world.counter}")


if __name__ == "__main__":
    main()