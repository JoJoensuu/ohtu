import requests
from player import Player
from datetime import datetime

def filter_by_points(player):
    return player.points

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
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

    print(f"Players from FIN {datetime.now()}\n\n")
    
    players.sort(key=lambda player: player.points, reverse=True)
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
