#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""

    if not boxes:
        return False
    if len(boxes) == 1:
        return True

    unlocked = set()
    queue = []

    unlocked.add(0)
    queue.extend(boxes[0])

    while queue:
        key = queue.pop()

        if key not in unlocked and key < len(boxes):
            unlocked.add(key)
            queue.extend(boxes[key])

    return len(unlocked) == len(boxes)
