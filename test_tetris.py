# -*- coding: utf-8 -*-
"""
@author: marwa
"""
import unittest
from tetris import can_place_piece, solve, visualize_tetris_solution

class TestTetrisPlacement(unittest.TestCase):

    def test_can_place_piece_valid(self):
        container = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        piece = [[1, 1], [1, 1]]
        self.assertTrue(can_place_piece(container, piece, 0, 0))

    def test_can_place_piece_invalid_collision(self):
        container = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        piece = [[1, 1], [1, 1]]
        self.assertFalse(can_place_piece(container, piece, 0, 0))

    def test_solve_valid_solution(self):
        M, N = 3, 3
        pieces = [[[1, 1], [1, 1]]]
        result = solve(M, N, pieces)
        expected_result = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(result, expected_result)
        visualize_tetris_solution(M, N, pieces)

    def test_visualize_tetris_solution(self):
        M, N = 3, 3
        pieces = [[[1, 1], [1, 1]]]
        # This is a visual test, so no direct assertion can be made.
        # Running the function to check for errors.
        visualize_tetris_solution(M, N, pieces)

if __name__ == '__main__':
    unittest.main()
