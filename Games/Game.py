from Games import GameStage


class Game():
    def __init__(self, name, password=None):
        self.name = name
        self.password = password

    players = []
    id = 0
    stage = GameStage.NOT_INITIALIZED

    @property
    def player_ct(self):
        return len(self.players)
