# -*- coding: utf-8 -*-

class TennisGameDefactored1:
    """
    A class representing a tennis game.

    Attributes:
        player1_name (str): The name of the first player.
        player2_name (str): The name of the second player.
        p1_points (int): The number of points scored by the first player.
        p2_points (int): The number of points scored by the second player.
        scores (dict): A dictionary to store the scores of both players.
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """
        Initializes a new tennis game with two players.

        Args:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player.
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores = {player1_name : 0, player2_name : 0}

    def won_point(self, player_name: str) -> None:
        """
        Increments the points of the player who won the point.

        Args:
            player_name (str): The name of the player who won the point.
        """
        try:
            self.scores[player_name] += 1
        except ValueError as e:
            raise ValueError(f"Значения нету в списке имён игроков': {str(e)}")

    def score(self) -> str:
        """
        Returns the current score of the game.

        Returns:
            str: The current score of the game.
        """
        score1, score2 = self.scores.values()

        if score1 == score2:
            return self._get_tied_score(score1)

        elif max(score1, score2) >= 4:
            return self._get_advantage_or_win_score(score1, score2)

        else:
            return self._get_separate_scores()

    def _get_tied_score(self, points: int) -> str:
        """
        Returns the score when both players have the same number of points.

        Args:
            points (int): The number of points both players have.

        Returns:
            str: The tied score representation.
        """

        POINTS_MAP = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All",
        }
        return POINTS_MAP.get(points, "Deuce")

    def _get_advantage_or_win_score(self, score1: int, score2: int) -> str:
        """
        Returns the score when one of the players has an advantage or wins.

        Args:
            score1 (int): The score of the first player.
            score2 (int): The score of the second player.

        Returns:
            str: The advantage or win representation.
        """

        minus_result = score1 - score2

        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_separate_scores(self, score1: int, score2: int) -> str:
        """
        Returns the score when both players have different points.

        Args:
            score1 (int): The score of the first player.
            score2 (int): The score of the second player.

        Returns:
            str: The separate scores representation.
        """
        scores = []

        for points in [(score1, self.player1_name), (score2, self.player2_name)]:
            score_map = {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }
            scores.append(score_map[points])
        return "-".join(scores)


class TennisGameDefactored2:
    """
    A class representing a tennis game.

    Attributes:
        player1_name (str): The name of the first player.
        player2_name (str): The name of the second player.
        p1_points (int): The number of points scored by the first player.
        p2_points (int): The number of points scored by the second player.
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """
        Initializes a new tennis game with two players.

        Args:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player.
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores = {player1_name : 0, player2_name : 0}

    def won_point(self, player_name: str) -> None:
        """
        Increments the points of the player who won the point.

        Args:
            player_name (str): The name of the player who won the point.
        """
        self.scores[player_name] += 1

    def score(self) -> str:
        """
        Returns the current score of the game.

        Returns:
            str: The current score of the game.
        """
        score1, score2 = self.scores.values()

        if score1 == score2:
            return self._handle_draw_score(score1)

        elif max(score1, score2) >= 4:
            return self._handle_win_or_advantage(score1, score2)

        else:
            return self._handle_regular_score(score1, score2)

    def _handle_draw_score(self, points: int) -> str:

        if points < 4:

            answer = ["Love", "Fifteen", "Thirty", "Forty"]
            return f"{answer[points]}-All"

        return "Deuce"

    def _handle_regular_score(self, score1: int, score2: int) -> str:

        score_names = ["Love", "Fifteen", "Thirty", "Forty"]

        p1_res = score_names[score1]
        p2_res = score_names[score2]

        return f"{p1_res}-{p2_res}"

    def _handle_win_or_advantage(self, score1: int, score2: int) -> str:

        if score1 >= 4 and (score1 - score2) >= 2:
            return f"Win for {self.player1_name}"

        if score2 >= 4 and (score2 - score1) >= 2:
            return f"Win for {self.player2_name}"

        if score1 > score2:
            return f"Advantage {self.player1_name}"

        return f"Advantage {self.player2_name}"

    def set_p1_score(self, number: int) -> None:
        """
        Sets the score of the first player.

        Args:
            number (int): The number of points to add to the first player's score.
        """
        self.scores[self.player1_name] += number

    def set_p2_score(self, number: int) -> None:
        """
        Sets the score of the second player.

        Args:
            number (int): The number of points to add to the second player's score.
        """
        self.scores[self.player2_name] += number


class TennisGameDefactored3:
    """
    A class representing a tennis game.

    Attributes:
        p1_name (str): The name of the first player.
        p2_name (str): The name of the second player.
        p1_points (int): The number of points scored by the first player.
        p2_points (int): The number of points scored by the second player.
    """

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """
        Initializes a new tennis game with two players.

        Args:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player.
        """
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name: str) -> None:
        """
        Increments the points of the player who won the point.

        Args:
            player_name (str): The name of the player who won the point.
        """
        if player_name == self.p1_name:
            self.p1_points += 1
        elif player_name == self.p2_name:
            self.p2_points += 1
        else:
            raise ValueError(f"Player {player_name} is not part of the game.")

    def score(self) -> str:
        """
        Returns the current score of the game.

        Returns:
            str: The current score of the game.
        """
        if self._is_game_in_progress():
            return self._get_regular_score()
        else:
            return self._get_final_score()

    def _is_game_in_progress(self) -> bool:
        """
        Checks if the game is still in progress (less than 4 points for both players).

        Returns:
            bool: True if the game is in progress, False otherwise.
        """
        return self.p1_points < 4 and self.p2_points < 4

    def _get_regular_score(self) -> str:
        """
        Returns the score when both players have less than 4 points.

        Returns:
            str: The current score in regular play.
        """
        points = ["Love", "Fifteen", "Thirty", "Forty"]
        score1 = points[self.p1_points]
        score2 = points[self.p2_points]
        return score1 + "-All" if self.p1_points == self.p2_points else f"{score1}-{score2}"

    def _get_final_score(self) -> str:
        """
        Returns the score when one player has 4 or more points.

        Returns:
            str: The final score indicating win or advantage.
        """
        if self.p1_points == self.p2_points:
            return "Deuce"

        winner = self.p1_name if self.p1_points > self.p2_points else self.p2_name
        score_difference = abs(self.p1_points - self.p2_points)

        if score_difference == 1:
            return f"Advantage {winner}"
        else:
            return f"Win for {winner}"
