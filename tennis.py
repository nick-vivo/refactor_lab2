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
        self.scores[player_name] += 1

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

        POINTS_MAP = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All",
        }
        return POINTS_MAP.get(points, "Deuce")

    def _get_advantage_or_win_score(self, score1, score2) -> str:

        minus_result = score1 - score2
        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_separate_scores(self, score1, score2) -> str:

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

    def _handle_draw_score(self, points) -> str:

        if points < 4:

            answer = ["Love", "Fifteen", "Thirty", "Forty"]
            return f"{answer[points]}-All"

        return "Deuce"

    def _handle_regular_score(self, score1, score2) -> str:

        score_names = ["Love", "Fifteen", "Thirty", "Forty"]

        p1_res = score_names[score1]
        p2_res = score_names[score2]

        return f"{p1_res}-{p2_res}"

    def _handle_win_or_advantage(self, score1, score2) -> str:

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
        p1 (int): The number of points scored by the first player.
        p2 (int): The number of points scored by the second player.
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
        self.p1 = 0
        self.p2 = 0

    def won_point(self, player_name: str) -> None:
        """
        Increments the points of the player who won the point.

        Args:
            player_name (str): The name of the player who won the point.
        """
        if player_name == self.p1_name:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self) -> str:
        """
        Returns the current score of the game.

        Returns:
            str: The current score of the game.
        """
        if self.p1 < 4 and self.p2 < 4:
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            score = points[self.p1]
            return score + "-All" if self.p1 == self.p2 else score + "-" + points[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            winner = self.p1_name if self.p1 > self.p2 else self.p2_name
            return f"Advantage {winner}" if (self.p1 - self.p2) ** 2 == 1 else f"Win for {winner}"


# NOTE: You must change this to point at the one of the three examples that you're working on!
TennisGame = TennisGameDefactored1
