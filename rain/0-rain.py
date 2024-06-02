#!/usr/bin/python3
"""
Rainwater Trapping Module

This module provides a function to calculate the amount of rainwater trapped
between walls after it rains. The calculation is based on the heights of the walls
provided as a list of non-negative integers.

Function:
    - rain(walls): Returns the total amount of rainwater retained.

Example usage:
    walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(rain(walls))  # Output: 6
"""


def rain(walls):
    """
    Calculate the total amount of rainwater retained between walls.

    Parameters:
    walls (list): A list of non-negative integers representing the heights of walls.

    Returns:
    int: The total amount of rainwater retained.
    """

    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_trapped = 0

    while left < right:
        if walls[left] < walls[right]:
            left_max = max(left_max, walls[left])
            water_trapped += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            water_trapped += right_max - walls[right]
            right -= 1

    return water_trapped


# Example usage:
if __name__ == "__main__":
    walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(rain(walls))  # Output: 6
