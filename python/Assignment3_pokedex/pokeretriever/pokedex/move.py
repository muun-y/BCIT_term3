from .pokedex_object import PokedexObject


class Move(PokedexObject):
    """
    Class representing a move in the Pokédex.

    Attributes:
        name (str): The name of the move.
        id (str): The ID of the move.
        generation (str): The generation of Pokémon games in which the move was introduced.
        accuracy (int): The accuracy of the move.
        pp (int): The power points (PP) of the move.
        power (int): The power of the move.
        type (str): The type of the move (e.g., "fire", "water").
        damage_class (str): The damage class of the move (e.g., "physical", "special").
        effect_short (str): A short description of the effect of the move.
    """

    def __init__(self, name: str, id: str, generation: str, accuracy: int, pp: int, power: int, type: str,
                 damage_class: str, effect_short: str):
        """
        Initialize a Move object.

        Args:
            name (str): The name of the move.
            id (str): The ID of the move.
            generation (str): The generation of Pokémon games in which the move was introduced.
            accuracy (int): The accuracy of the move.
            pp (int): The power points (PP) of the move.
            power (int): The power of the move.
            type (str): The type of the move (e.g., "fire", "water").
            damage_class (str): The damage class of the move (e.g., "physical", "special").
            effect_short (str): A short description of the effect of the move.
        """
        super().__init__(name, id)
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type
        self.damage_class = damage_class
        self.effect_short = effect_short

    def __str__(self):
        """
        Return a string representation of the Move object.

        Returns:
            str: A formatted string containing information about the move.
        """
        return f"Name: {self.name}\n" \
            f"ID: {self.id}\n" \
            f"Generation: {self.generation}\n" \
            f"Accuracy: {self.accuracy}\n" \
            f"PP: {self.pp}\n" \
            f"Power: {self.power}\n" \
            f"Type: {self.type}\n" \
            f"Damage class: {self.damage_class}\n" \
            f"Effect (Short): {self.effect_short}\n"
