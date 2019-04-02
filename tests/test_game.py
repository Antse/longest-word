# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_valid_is_empty(self):
        new_game = Game()
        new_game.grid = ["A","B","C"]
        self.assertEqual(new_game.is_valid(""),False)

    def test_is_valid_is_not_in_grid(self):
        new_game = Game()
        new_game.grid = ["A","B","C"]
        self.assertEqual(new_game.is_valid("DER"),False)

    def test_is_valid_does_not_enougth_letter_grid(self):
        new_game = Game()
        new_game.grid = ["A","B","C"]
        self.assertEqual(new_game.is_valid("AABBCC"),False)



    def random_grid():
        pass


