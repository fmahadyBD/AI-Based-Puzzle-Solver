

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

class PuzzleSolver:

    def __init__(self, start_state):
        self.start_state = start_state

if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [5, 7, 6],
        [4, 0, 8]
    ]