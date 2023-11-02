from queue import PriorityQueue

goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)

initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]
            if tile != 0:
                goal_position = goal_state.index(tile)
                goal_row, goal_col = goal_position // 3, goal_position % 3
                current_row, current_col = i, j
                distance += abs(goal_row - current_row) + abs(goal_col - current_col)
    return distance

def get_possible_moves(state):
    moves = []
    empty_position = state.index(0)
    row, col = empty_position // 3, empty_position % 3
    if row > 0:
        moves.append(empty_position - 3)  
    if row < 2:
        moves.append(empty_position + 3)  
    if col > 0:
        moves.append(empty_position - 1)  
    if col < 2:
        moves.append(empty_position + 1)  
    return moves

def solve_puzzle(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {initial_state: 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == goal_state:

            path = []
            while current_state in came_from:
                path.append(current_state)
                current_state = came_from[current_state]
            path.append(initial_state)
            path.reverse()
            return path

        for next_position in get_possible_moves(current_state):
            new_state = list(current_state)
            new_state[current_state.index(0)], new_state[next_position] = new_state[next_position], new_state[current_state.index(0)]
            new_state = tuple(new_state)
            new_cost = cost_so_far[current_state] + 1

            if new_state not in cost_so_far or new_cost < cost_so_far[new_state]:
                cost_so_far[new_state] = new_cost
                priority = new_cost + manhattan_distance(new_state)
                frontier.put((priority, new_state))
                came_from[new_state] = current_state

    return None

solution = solve_puzzle(initial_state)

if solution:
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found.")
