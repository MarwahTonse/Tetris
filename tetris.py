import matplotlib.pyplot as plt
import numpy as np
import random

def initialize_container(M, N):
    return [[0] * N for _ in range(M)]

def can_place_piece(container, piece, row, col):
    piece_rows = len(piece)
    piece_cols = len(piece[0])

    for r in range(piece_rows):
        for c in range(piece_cols):
            if piece[r][c] == 1:
                container_row = row + r
                container_col = col + c

                if (
                    container_row >= len(container)
                    or container_col >= len(container[0])
                    or container[container_row][container_col] != 0  # Check if the cell is already occupied
                ):
                    return False
    return True


def place_piece(container, piece, row, col, piece_id):
    piece_rows = len(piece)
    piece_cols = len(piece[0])

    for r in range(piece_rows):
        for c in range(piece_cols):
            if piece[r][c] == 1:
                container[row + r][col + c] = piece_id

def solve(M, N, pieces):
    container = initialize_container(M, N)
    piece_id = 0

    for piece in pieces:
        piece_id += 1
        placed = False

        for row in range(M - 1, -1, -1):
            if placed:
                break

            for col in range(N):
                if col + len(piece[0]) <= N and can_place_piece(container, piece, row, col):
                    place_piece(container, piece, row, col, piece_id)
                    placed = True
                    break

            if placed:
                break

    return container

def cost_function(container):
    # Count the number of empty cells in the container
    empty_cells = sum(row.count(0) for row in container)

    # The lower the number of empty cells, the better the fit
    return empty_cells

'''
 A better solution would have fewer empty cells in the container, 
 meaning that more pieces are placed, and the placement is more compact.
'''
def solve_with_cost(M, N, pieces):
    container = initialize_container(M, N)
    piece_id = 0

    for piece in pieces:
        piece_id += 1
        placed = False

        for row in range(M - 1, -1, -1):
            if placed:
                break

            for col in range(N):
                if col + len(piece[0]) <= N and can_place_piece(container, piece, row, col):
                    place_piece(container, piece, row, col, piece_id)
                    placed = True
                    break

            if placed:
                break

    cost = cost_function(container)
    return container, cost


def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def visualize_tetris_solution(M, N, pieces):
    container_rows = M
    container_cols = N

    plt.figure(figsize=(8, 6))
    plt.title("Tetris Piece Placement")
    plt.axis("off")

    # Create a dictionary to store colors for each piece
    piece_colors = {}

    for step, piece in enumerate(pieces, start=1):
        plt.clf()  # Clear the previous plot

        # Copy the current pieces to avoid modifying the original list
        current_pieces = pieces[:step]

        # Place the current piece in the container
        result, cost = solve_with_cost(M, N, current_pieces)
        colored_container = np.zeros((container_rows, container_cols, 3), dtype=np.uint8)

        for row in range(container_rows):
            for col in range(container_cols):
                piece_id = result[row][col]
                if piece_id != 0:
                    if piece_id not in piece_colors:
                        # Convert piece_id to a tuple before using it as a key
                        piece_colors[piece_id] = random_color()

                    colored_container[row][col] = tuple(int(piece_colors[piece_id][i:i+2], 16) for i in (1, 3, 5))
        plt.imshow(colored_container)
        plt.pause(1)  # Pause to visualize each step
        plt.show()
    print('To check the goodness of fit, we can count the number of empty cells. The number of empty cells are: ', cost)            



# Example input
M = 7
N = 8
pieces = [
    [[1, 1], [1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]]
]

# Visualize the Tetris solution with each piece having a unique color
visualize_tetris_solution(M, N, pieces)
