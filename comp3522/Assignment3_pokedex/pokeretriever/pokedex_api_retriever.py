from .request import Request
from .pokedex_object_generate import generate_pokedex_object
import aiohttp
from datetime import datetime


class PokeAPIRetriever:
    """
    Class for retrieving data from the PokeAPI.

    Attributes:
        POKEMON_API_END_POINT (str): The base URL of the PokeAPI endpoint.
        poke_request (Request): An instance of the Request class for handling API requests.
    """

    # PokeAPI endpoint
    # The first placeholder is the mode (pokemon, ability, move, stat)
    # The second placeholder is the input data (name or ID)
    POKEMON_API_END_POINT = "https://pokeapi.co/api/v2/{}/{}"

    def __init__(self):
        """
        Initialize a PokeAPIRetriever object.
        """
        self.poke_request = Request()

    async def execute_request(self) -> None:
        """
        Execute the API request and process the response.

        Raises:
            Exception: An exception occurred during the request execution.
        """
        try:
            output_objects = []
            for item in self.poke_request.input_data:
                async with aiohttp.ClientSession() as session:
                    async with session.get(PokeAPIRetriever.POKEMON_API_END_POINT.format(self.poke_request.mode, item.strip())) as response:
                        data = await response.json()
                        output_object = await generate_pokedex_object(self.poke_request, data)
                        output_objects.append(output_object)
            if self.poke_request.output_file:
                self.write_output_to_file(output_objects)
            else:
                for obj in output_objects:
                    print("obj", obj)

        except Exception as e:
            print("error", e)

    def write_output_to_file(self, pokedex_objects):
        """
        Write the retrieved data to a text file.

        Args:
            pokedex_objects (list): A list of PokedexObject instances.

        Raises:
            IOError: An error occurred while writing to the file.
        """
        try:
            with open(self.poke_request.output_file, 'w', encoding='UTF-8') as output_text_file:
                # Write Timestamp
                timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
                output_text_file.write(f"Timestamp: {timestamp}\n")

                # Write Number of requests
                num_requests = len(self.poke_request.input_data)
                output_text_file.write(
                    f"Number of requests: {num_requests}\n\n")

                # Write pokedex objects
                for pokedex_object in pokedex_objects:
                    output_text_file.write(pokedex_object.__str__() + "\n")

            print(
                f"Completed writing output to {self.poke_request.output_file}.")
        except IOError:
            print("Error with writing to text file, exiting program.")
        finally:
            exit(0)
