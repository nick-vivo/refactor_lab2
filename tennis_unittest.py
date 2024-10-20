# -*- coding: utf-8 -*-

import unittest

from tennis import TennisGameDefactored1, TennisGameDefactored2, TennisGameDefactored3


class TestTennisGameDefactored3(unittest.TestCase):

    def setUp(self):
        """Create a new game before each test."""
        self.game = TennisGameDefactored3("player1", "player2")

    def test_initial_score(self):
        """Test the initial score of the game."""
        self.assertEqual(self.game.score(), "Zero-All")

    def test_score_after_one_point(self):
        """Test the score after player1 wins one point."""
        self.game.won_point("player1")
        self.assertEqual(self.game.score(), "One-Zero")

    def test_score_after_two_points(self):
        """Test the score after player2 wins one point."""
        self.game.won_point("player1")
        self.game.won_point("player2")
        self.assertEqual(self.game.score(), "One-All")

    def test_score_after_multiple_points(self):
        """Test the score after various points."""
        for _ in range(3):
            self.game.won_point("player1")
        for _ in range(2):
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Three-Two")

    def test_win_condition_player1(self):
        """Test win condition for player1."""
        for _ in range(4):
            self.game.won_point("player1")
        self.assertEqual(self.game.score(), "Win for player1")

    def test_win_condition_player2(self):
        """Test win condition for player2."""
        for _ in range(4):
            self.game.won_point("player2")
        self.assertEqual(self.game.score(), "Win for player2")

    def test_advantage_player1(self):

        """Test advantage condition for player1."""
        for _ in range(3):
            self.game.won_point("player1")
        for _ in range(4):
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Advantage player2")
        self.game.won_point("player1")
        self.assertEqual(self.game.score(), "Deuce")

    def test_deuce(self):
        """Test deuce condition."""
        for _ in range(3):
            self.game.won_point("player1")
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Three-All")

    def test_invalid_player(self):
        """Test invalid player raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.game.won_point("invalid_player")
        self.assertEqual(str(context.exception), "Player invalid_player is not part of the game.")

    def test_score_with_high_points(self):
        """Test score with high points."""
        self.game.p1_points = 6
        self.game.p2_points = 4
        self.assertEqual(self.game.score(), "Win for player1")

        self.game.p1_points = 4
        self.game.p2_points = 6
        self.assertEqual(self.game.score(), "Win for player2")

    def test_advantage_with_high_points(self):
        """Test advantage with high points."""
        self.game.p1_points = 5
        self.game.p2_points = 4 
        self.assertEqual(self.game.score(), "Advantage player1")

        self.game.p1_points = 4 
        self.game.p2_points = 5
        self.assertEqual(self.game.score(), "Advantage player2")


class TestTennisGameDefactored2(unittest.TestCase):

    def setUp(self):
        """Create a new game before each test."""
        self.game = TennisGameDefactored2("player1", "player2")

    def test_initial_score(self):
        """Test the initial score of the game."""
        self.assertEqual(self.game.score(), "Zero-All")

    def test_score_after_one_point(self):
        """Test the score after player1 wins one point."""
        self.game.won_point("player1")
        self.assertEqual(self.game.score(), "One-Zero")

    def test_score_after_two_points(self):
        """Test the score after player2 wins one point."""
        self.game.won_point("player1")
        self.game.won_point("player2")
        self.assertEqual(self.game.score(), "One-All")

    def test_score_after_multiple_points(self):
        """Test the score after various points."""
        for _ in range(3):
            self.game.won_point("player1")
        for _ in range(2):
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Three-Two")

    def test_win_condition_player1(self):
        """Test win condition for player1."""
        for _ in range(4):
            self.game.won_point("player1")
        self.assertEqual(self.game.score(), "Win for player1")

    def test_win_condition_player2(self):
        """Test win condition for player2."""
        for _ in range(4):
            self.game.won_point("player2")
        self.assertEqual(self.game.score(), "Win for player2")

    def test_advantage_player1(self):

        """Test advantage condition for player1."""
        for _ in range(3):
            self.game.won_point("player1")
        for _ in range(4):
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Advantage player2")
        self.game.won_point("player1")
        self.assertEqual(self.game.score(), "Deuce")

    def test_deuce(self):
        """Test deuce condition."""
        for _ in range(3):
            self.game.won_point("player1")
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Three-All")

    def test_score_with_high_points(self):
        """Test score with high points."""
        self.game.scores[self.game.player1_name] = 6
        self.game.scores[self.game.player2_name] = 4
        self.assertEqual(self.game.score(), "Win for player1")

        self.game.scores[self.game.player1_name] = 4
        self.game.scores[self.game.player2_name] = 6
        self.assertEqual(self.game.score(), "Win for player2")

    def test_advantage_with_high_points(self):
        """Test advantage with high points."""
        self.game.scores[self.game.player1_name] = 5
        self.game.scores[self.game.player2_name] = 4
        self.assertEqual(self.game.score(), "Advantage player1")

        self.game.scores[self.game.player1_name] = 4
        self.game.scores[self.game.player2_name] = 5
        self.assertEqual(self.game.score(), "Advantage player2")


class TestTennisGameDefactored1(unittest.TestCase):

    def setUp(self):
        """Create a new game before each test."""
        self.game = TennisGameDefactored1("player1", "player2")

    def test_initial_score(self):
        """Test the initial score of the game."""
        self.assertEqual(self.game.score(), "Zero-All")

    def test_score_after_one_point(self):
        """Test the score after player1 wins one point."""
        self.game.won_point("player1")
        self.assertEqual(self.game.score(), "One-Zero")

    def test_score_after_two_points(self):
        """Test the score after player2 wins one point."""
        self.game.won_point("player1")
        self.game.won_point("player2")
        self.assertEqual(self.game.score(), "One-All")

    def test_score_after_multiple_points(self):
        """Test the score after various points."""
        for _ in range(3):
            self.game.won_point("player1")
        for _ in range(2):
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Three-Two")

    def test_win_condition_player1(self):
        """Test win condition for player1."""
        for _ in range(4):
            self.game.won_point("player1")
        self.assertEqual(self.game.score(), "Win for player1")

    def test_win_condition_player2(self):
        """Test win condition for player2."""
        for _ in range(4):
            self.game.won_point("player2")
        self.assertEqual(self.game.score(), "Win for player2")

    def test_advantage_player1(self):

        """Test advantage condition for player1."""
        for _ in range(3):
            self.game.won_point("player1")
        for _ in range(4):
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Advantage player2")
        self.game.won_point("player1")
        self.assertEqual(self.game.score(), "Deuce")

    def test_deuce(self):
        """Test deuce condition."""
        for _ in range(3):
            self.game.won_point("player1")
            self.game.won_point("player2")

        self.assertEqual(self.game.score(), "Three-All")

    def test_score_with_high_points(self):
        """Test score with high points."""
        self.game.scores[self.game.player1_name] = 6
        self.game.scores[self.game.player2_name] = 4
        self.assertEqual(self.game.score(), "Win for player1")

        self.game.scores[self.game.player1_name] = 4
        self.game.scores[self.game.player2_name] = 6
        self.assertEqual(self.game.score(), "Win for player2")

    def test_advantage_with_high_points(self):
        """Test advantage with high points."""
        self.game.scores[self.game.player1_name] = 5
        self.game.scores[self.game.player2_name] = 4
        self.assertEqual(self.game.score(), "Advantage player1")

        self.game.scores[self.game.player1_name] = 4
        self.game.scores[self.game.player2_name] = 5
        self.assertEqual(self.game.score(), "Advantage player2")


if __name__ == "__main__":
    unittest.main()
