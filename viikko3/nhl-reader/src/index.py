import requests
from player import Player
from datetime import datetime

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url).json()

    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
            )

            players.append(player)
        print(player)
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        playah = [player for player in self.players if player.nationality == nationality]
        playah.sort(key=lambda player:player.points, reverse=True)
        return playah

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print(f"Players from FIN {datetime.now()}\n\n")
    
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
