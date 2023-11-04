from collections import deque

def is_valid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3 or (m < c and m > 0) or (3 - m < 3 - c and 3 - m > 0):
        return False
    return True

def goal_state(state):
    return state == (0, 0, 0)

def successors(state):
    m, c, b = state
    actions = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]
    if b == 1:
        actions = [(-a, -b) for a, b in actions]

    valid_successors = []
    for a, b in actions:
        new_state = (m + a, c + b, 1 - b)
        if is_valid(new_state):
            valid_successors.append(new_state)

    return valid_successors

def bfs(start):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()
        if goal_state(state):
            return path
        visited.add(state)

        for successor in successors(state):
            if successor not in visited:
                queue.append((successor, path + [successor]))

    return None

start_state = (3, 3, 1)
solution = bfs(start_state)

if solution:
    for i, step in enumerate(solution):
        print(f"Step {i + 1}: {step}")
else:
    print("No solution found.")
