import abc


class PokedexObject(abc.ABC):
    """Base class for objects representing entities in the Pokedex.

    Attributes:
        name (str): The name of the entity.
        id (str): The ID of the entity.
    """

    def __init__(self, name: str, id: str):
        """Initialize a PokedexObject with a name and an ID.

        Args:
            name (str): The name of the entity.
            id (str): The ID of the entity.
        """
        self.name = name
        self.id = id
