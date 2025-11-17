from collections import deque

def water_jug_bfs(jugX, jugY, goal):
    start = (0, 0)
    visited = set([start])
    queue = deque([(start, [])])  # (state, path)

    while queue:
        (x, y), path = queue.popleft()

        # Goal check
        if x == goal or y == goal:
            return path + [(x, y)]

        # All possible next moves
        next_states = [
            (jugX, y),            # Fill X
            (x, jugY),            # Fill Y
            (0, y),               # Empty X
            (x, 0),               # Empty Y
            (x - min(x, jugY - y), y + min(x, jugY - y)),  # X → Y
            (x + min(y, jugX - x), y - min(y, jugX - x))   # Y → X
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(x, y)]))

    return None


# ---- DRIVER CODE ----
jugX = 4
jugY = 3
goal = 2

solution = water_jug_bfs(jugX, jugY, goal)

if solution:
    print("Solution Steps:")
    for s in solution:
        print(s)
else:
    print("No solution exists.")
