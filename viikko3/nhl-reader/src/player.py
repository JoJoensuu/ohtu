class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = goals + assists
    
    def __str__(self):
        return f"{self.name:20}{self.team} {self.goals} + {self.assists} = {self.points}"

    def return_points(self):
        return self.points