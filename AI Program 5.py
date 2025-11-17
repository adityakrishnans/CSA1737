from collections import deque

def is_valid(mL, cL, mR, cR):
    if not (0 <= mL <= 3 and 0 <= cL <= 3 and 0 <= mR <= 3 and 0 <= cR <= 3):
        return False
    if (mL > 0 and mL < cL):  # Left bank invalid
        return False
    if (mR > 0 and mR < cR):  # Right bank invalid
        return False
    return True

def solve():
    start = (3, 3, 0, 0, 'L')
    goal = (0, 0, 3, 3, 'R')

    queue = deque([(start, [start])])
    visited = set([start])

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]  # (M,C)

    while queue:
        (mL, cL, mR, cR, boat), path = queue.popleft()

        if (mL, cL, mR, cR, boat) == goal:
            return path

        for m, c in moves:
            if boat == 'L':    # Move from left to right
                new_state = (mL - m, cL - c, mR + m, cR + c, 'R')
            else:              # Move from right to left
                new_state = (mL + m, cL + c, mR - m, cR - c, 'L')

            if is_valid(*new_state[:4]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

# ---- DRIVER CODE ----
solution = solve()

if solution:
    print("Solution Path:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
