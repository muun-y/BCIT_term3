from .pokedex_object import PokedexObject


class Ability(PokedexObject):
    """
    Class representing an ability in the Pokédex.

    Attributes:
        name (str): The name of the ability.
        id (str): The ID of the ability.
        generation (str): The generation of Pokémon games in which the ability was introduced.
        effect (str): The detailed effect description of the ability.
        effect_short (str): A short description of the effect of the ability.
        pokemon (list): A list of Pokémon that have this ability.
    """

    def __init__(self, name: str, id: str, generation: str, effect: str, effect_short: str, pokemon: list):
        """
        Initialize an Ability object.

        Args:
            name (str): The name of the ability.
            id (str): The ID of the ability.
            generation (str): The generation of Pokémon games in which the ability was introduced.
            effect (str): The detailed effect description of the ability.
            effect_short (str): A short description of the effect of the ability.
            pokemon (list): A list of Pokémon that have this ability.
        """
        super().__init__(name, id)
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        """
        Return a string representation of the Ability object.

        Returns:
            str: A formatted string containing information about the ability.
        """
        pokemon_str = ", ".join(self.pokemon)
        return f"Name: {self.name}\n" \
            f"ID: {self.id}\n" \
            f"Generation: {self.generation}\n" \
            f"Effect: {self.effect}\n" \
            f"Effect (Short): {self.effect_short}\n" \
            f"Pokemon: {pokemon_str}\n"
