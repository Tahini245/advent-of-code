from collections import deque


def main(days: int):
    # Value of internal counter determined using Ctrl + F on input
    fish = deque((0, 114, 47, 51, 36, 52, 0, 0, 0))
    for _ in range(days):
        fish.append(fish.popleft())
        fish[-3] += fish[-1]
    return sum(fish)
