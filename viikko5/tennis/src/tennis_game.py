class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

        self.points_per_round = 1
        self.endgame_points = 4

        self.ties = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce", "Deuce"]
        self.score_terms = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += self.points_per_round
        elif player_name == self.player2_name:
            self.player2_score += self.points_per_round

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.create_tie_score_string()
        elif max(self.player1_score, self.player2_score) >= self.endgame_points:
            return self.create_endgame_score_string()
        else:
            return self.create_midgame_score_string()

    def create_midgame_score_string(self):
        return f"{self.score_terms[self.player1_score]}-{self.score_terms[self.player2_score]}"

    def create_endgame_score_string(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def create_tie_score_string(self):
        return self.ties[self.player1_score]