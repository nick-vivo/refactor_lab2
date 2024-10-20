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
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name: str) -> None:
        """
        Increments the points of the player who won the point.

        Args:
            player_name (str): The name of the player who won the point.
        """
        if player_name == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def score(self) -> str:
        """
        Returns the current score of the game.

        Returns:
            str: The current score of the game.
        """
        result = ""
        if self.p1_points == self.p2_points and self.p1_points < 4:
            if self.p1_points == 0:
                result = "Love"
            if self.p1_points == 1:
                result = "Fifteen"
            if self.p1_points == 2:
                result = "Thirty"
            if self.p1_points == 3:
                result = "Forty"
            result += "-All"
        if self.p1_points == self.p2_points and self.p1_points >= 4:
            result = "Deuce"

        p1_res = ""
        p2_res = ""
        if self.p1_points > 0 and self.p2_points == 0:
            if self.p1_points == 1:
                p1_res = "Fifteen"
            if self.p1_points == 2:
                p1_res = "Thirty"
            if self.p1_points == 3:
                p1_res = "Forty"
            p2_res = "Love"
            result = p1_res + "-" + p2_res
        if self.p2_points > 0 and self.p1_points == 0:
            if self.p2_points == 1:
                p2_res = "Fifteen"
            if self.p2_points == 2:
                p2_res = "Thirty"
            if self.p2_points == 3:
                p2_res = "Forty"
            p1_res = "Love"
            result = p1_res + "-" + p2_res

        if self.p1_points > self.p2_points and self.p1_points < 4:
            if self.p1_points == 2:
                p1_res = "Thirty"
            if self.p1_points == 3:
                p1_res = "Forty"
            if self.p2_points == 1:
                p2_res = "Fifteen"
            if self.p2_points == 2:
                p2_res = "Thirty"
            result = p1_res + "-" + p2_res
        if self.p2_points > self.p1_points and self.p2_points < 4:
            if self.p2_points == 2:
                p2_res = "Thirty"
            if self.p2_points == 3:
                p2_res = "Forty"
            if self.p1_points == 1:
                p1_res = "Fifteen"
            if self.p1_points == 2:
                p1_res = "Thirty"
            result = p1_res + "-" + p2_res

        if self.p1_points > self.p2_points and self.p2_points >= 3:
            result = f"Advantage {self.player1_name}"
        if self.p2_points > self.p1_points and self.p1_points >= 3:
            result = f"Advantage {self.player2_name}"
        if self.p1_points >= 4 and self.p2_points >= 0 and (self.p1_points - self.p2_points) >= 2:
            result = f"Win for {self.player1_name}"
        if self.p2_points >= 4 and self.p1_points >= 0 and (self.p2_points - self.p1_points) >= 2:
            result = f"Win for {self.player2_name}"
        return result

    def set_p1_score(self, number: int) -> None:
        """
        Sets the score of the first player.

        Args:
            number (int): The number of points to add to the first player's score.
        """
        for _ in range(number):
            self.p1_score()

    def set_p2_score(self, number: int) -> None:
        """
        Sets the score of the second player.

        Args:
            number (int): The number of points to add to the second player's score.
        """
        for _ in range(number):
            self.p2_score()

    def p1_score(self) -> None:
        """
        Increments the score of the first player.
        """
        self.p1_points += 1

    def p2_score(self) -> None:
        """
        Increments the score of the second player.
        """
        self.p2_points += 1


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
