class PlayerStats:
    def __init__(self, reader) -> None:
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = []
        for player in sorted(self.reader.get_players(), key=lambda player : player.goals + player.assists, reverse=True):
            if player.nationality == nationality:
                players.append(player)
        return players