from .pokedex_object import PokedexObject


class Pokemon(PokedexObject):
    """
    Class representing a Pokémon in the Pokédex.

    Attributes:
        name (str): The name of the Pokémon.
        id (str): The ID of the Pokémon.
        height (int): The height of the Pokémon.
        weight (int): The weight of the Pokémon.
        stats (list or dict): The stats of the Pokémon. If a dict, it contains the stat names as keys and their values.
            If a list, it contains additional information about the stats.
        types (list): The types of the Pokémon.
        abilities (list): The abilities of the Pokémon.
        moves (list): The moves of the Pokémon.
    """

    def __init__(self, name: str, id: str, height: int, weight: int, stats: list, types: list, abilities: list,
                 moves: list):
        """
        Initialize a Pokemon object.

        Args:
            name (str): The name of the Pokémon.
            id (str): The ID of the Pokémon.
            height (int): The height of the Pokémon.
            weight (int): The weight of the Pokémon.
            stats (list or dict): The stats of the Pokémon.
            types (list): The types of the Pokémon.
            abilities (list): The abilities of the Pokémon.
            moves (list): The moves of the Pokémon.
        """
        super().__init__(name, id)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        """
        Return a string representation of the Pokemon object.

        Returns:
            str: A formatted string containing information about the Pokémon.
        """

        # Stat
        if isinstance(self.stats, dict):
            stats_string = "\n-------\n\n" + \
                '\n'.join(f"('{key}', {val})" for key,
                          val in self.stats.items()) \
                + "\n"
        else:
            stats_string = "\n-------\n" + "\n".join(self.stats) + "\n-------"

        # Ability
        abilities_string = "\n-------\n" + \
            "\n".join(self.abilities) + "\n-------"

        # Move
        moves_string = "\n-------\n\n"
        for move in self.moves:
            if isinstance(move, dict):
                moves_string += f"('Move name: {move['Move name']}', 'Level acquired: {move['Level acquired']}')" \
                    + "\n\n"
            else:
                moves_string += "\n".join(self.moves) + "\n-------"

        # Type
        types_string = ", ".join(self.types)

        return f"Name: {self.name}\n" \
            f"ID: {self.id}\n" \
            f"Height: {self.height}\n" \
            f"Weight: {self.weight}\n" \
            f"Types: {types_string}\n\n" \
            f"Stats: {stats_string}\n" \
            f"Abilities: {abilities_string}\n\n" \
            f"Moves: {moves_string}"
