import heapq

goal = "123456780"

def manhattan(state):
    dist = 0
    for i, c in enumerate(state):
        if c != "0":
            g = goal.index(c)
            dist += abs(i//3 - g//3) + abs(i%3 - g%3)
    return dist

def get_neighbors(state):
    neighbors = []
    i = state.index("0")
    r, c = i//3, i%3
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr*3 + nc
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            neighbors.append("".join(lst))
    return neighbors

def solve(start):
    pq = [(manhattan(start), start, None)]  # (priority, state, parent)
    visited = {start: None}
    while pq:
        _, state, parent = heapq.heappop(pq)
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = visited[state]
            return path[::-1]
        for nxt in get_neighbors(state):
            if nxt not in visited:
                visited[nxt] = state
                heapq.heappush(pq, (manhattan(nxt), nxt, state))
    return None

# --- DRIVER CODE ---
start = "125340678"   # Example input
solution = solve(start)

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        print(step[0:3], "\n" + step[3:6], "\n" + step[6:9], "\n")
else:
    print("No solution exists.")
