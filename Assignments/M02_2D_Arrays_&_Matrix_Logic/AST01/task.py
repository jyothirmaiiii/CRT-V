from typing import List


def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    result = []

    total = rows * cols
    r, c = rStart, cStart

    # Starting position
    result.append([r, c])

    # East, South, West, North
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    direction = 0
    step_length = 1

    while len(result) < total:

        # Each step length is used twice
        for _ in range(2):

            dr, dc = directions[direction]

            for _ in range(step_length):
                r += dr
                c += dc

                # Add only positions inside the grid
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])

                if len(result) == total:
                    return result

            direction = (direction + 1) % 4

        step_length += 1

    return result