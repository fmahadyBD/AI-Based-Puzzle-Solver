import copy
import time
from collections import deque

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  
]

MOVES = {
    'Up': (-1, 0),
    'Down': (1, 0),
    'Left': (0, -1),
    'Right': (0, 1)
}

# Object reference self
# Set instance variable self.a

class PuzzleSolver:
    def __init__(self, start_state):
        self.start_state = start_state

    def is_goal(self, state):
        return state == GOAL_STATE

    def find_zero(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def generate_neighbors(self, state):
        neighbors = []
        x, y = self.find_zero(state)

        for move, (dx, dy) in MOVES.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = copy.deepcopy(state)
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append((new_state, move))

        return neighbors

    def bfs(self):
        visited = set()
        queue = deque()
        queue.append((self.start_state, []))  # (state, path)

        while queue:
            current_state, path = queue.popleft()
            state_tuple = tuple(map(tuple, current_state))

            if state_tuple in visited:
                continue

            visited.add(state_tuple)

            if self.is_goal(current_state):
                return path

            for neighbor, move in self.generate_neighbors(current_state):
                queue.append((neighbor, path + [move]))

        return None

    

    def print_puzzle(self, state):
        for row in state:
            print(" ".join(str(num) if num != 0 else "_" for num in row))
        print()

    def replay_solution(self, moves):
        current_state = copy.deepcopy(self.start_state)
        print("Initial State:")
        self.print_puzzle(current_state)
        time.sleep(1)

        for move in moves:
            x, y = self.find_zero(current_state)
            dx, dy = MOVES[move]
            nx, ny = x + dx, y + dy
            current_state[x][y], current_state[nx][ny] = current_state[nx][ny], current_state[x][y]
            print(f"Move: {move}")
            self.print_puzzle(current_state)
            time.sleep(0.8)  

if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [5, 7, 6],
        [4, 0, 8]
    ]

    solver = PuzzleSolver(start)

    print("Solving using BFS...\n")
    bfs_solution = solver.bfs()
    if bfs_solution:
        print(f"Solution found with {len(bfs_solution)} moves: {bfs_solution}\n")
        solver.replay_solution(bfs_solution)
    else:
        print("No solution found using BFS.")
