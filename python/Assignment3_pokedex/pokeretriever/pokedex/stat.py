from .pokedex_object import PokedexObject


class Stat(PokedexObject):
    """
    Class representing a stat in the Pokédex.

    Attributes:
        name (str): The name of the stat.
        id (str): The ID of the stat.
        is_battle_only (bool): Indicates whether the stat is exclusive to battles.
    """

    def __init__(self, name: str, id: str, is_battle_only: bool, move_damage_class: str):
        """
        Initialize a Stat object.

        Args:
            name (str): The name of the stat.
            id (str): The ID of the stat.
            is_battle_only (bool): Indicates whether the stat is exclusive to battles.
        """
        super().__init__(name, id)
        self.is_battle_only = is_battle_only
        self.move_damage_class = move_damage_class

    def __str__(self):
        """
        Return a string representation of the Stat object.

        Returns:
            str: A formatted string containing information about the stat.
        """
        return f"Name: {self.name}\n" \
            f"ID: {self.id}\n" \
            f"Is_Battle_Only: {self.is_battle_only}\n" \
            f"Move Damage Class: {self.move_damage_class}\n"
