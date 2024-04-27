from enum import Enum


class RequestMode(Enum):
    """
    Enumeration class representing different modes for making requests to the PokeAPI.

    Attributes:
        POKEMON (str): Mode for requesting Pokemon data.
        ABILITY (str): Mode for requesting ability data.
        MOVE (str): Mode for requesting move data.
        STAT (str): Mode for requesting stat data.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
    STAT = "stat"
