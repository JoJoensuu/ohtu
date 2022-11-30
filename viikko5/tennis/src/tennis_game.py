class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_score_even(self.player1_score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_score_more_than_four()
        else:
            return self.get_score_less_than_four()

    def get_score_even(self, score):
        if score >= 4:
            return "Deuce"
        text_score = self.get_score_for_single_player(score)
        return f"{text_score}-All"

    def get_score_more_than_four(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_score_less_than_four(self):
        score_player_1 = self.get_score_for_single_player(self.player1_score)
        score_player_2 = self.get_score_for_single_player(self.player2_score)
        return f"{score_player_1}-{score_player_2}"

    def get_score_for_single_player(self, player_score):
        if player_score >= 4:
            return ""
        elif player_score == 0:
            return "Love"
        elif player_score == 1:
            return "Fifteen"
        elif player_score == 2:
            return "Thirty"
        elif player_score == 3:
            return "Forty"      