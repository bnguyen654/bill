from enum import Enum


class GameStage(Enum):
    NOT_INITIALIZED = 0
    PRE_START = 1
    ROLE_SELECTION = 2
    PLAYING = 3
    ENDGAME = 4
    DONE = 5
