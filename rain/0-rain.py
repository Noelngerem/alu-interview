#!/usr/bin/python3

def rain(walls):
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

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(rain(walls))
