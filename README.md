# Tetris

This repository contains a simple Tetris puzzle solver implemented in Python. The solver uses a basic algorithm to place Tetris pieces in a container with the goal of optimizing the placement.

## Requirements
- Python 3.8
- Matplotlib
- NumPy

## Installation
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/MarwahTonse/Tetris.git
   ```
2. Change directory
   ```
   cd Tetris-main
   ```
## Usage
Run the main Tetris solver script with the following command:
```bash
python tetris.py
```
This script visualizes the Tetris puzzle-solving process, placing each piece in the container step by step.

Run the main Tetris test script with the following command:
```bash
python test_tetris.py
```
This script provides unit test cases.

## Configuration
You can customize the Tetris puzzle by modifying the M, N, and pieces variables in the tetris_solver.py script.

## Visualization
The script uses Matplotlib to visualize the Tetris piece placement. Each piece is assigned a unique color for better clarity.
