from enum import Enum


class State(Enum):
    HELLO = 0
    PLAY = 1

    
State.ALL = tuple(State)
