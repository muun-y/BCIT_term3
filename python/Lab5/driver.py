# Name: Mun Young Cho
# Student number: A01330048

import json
from driver import *
from file_handler import FileHandler, FileExtensions, InvalidFileTypeError

"""
Custom exception class to handle cases where the word is not found.
"""


class WordNotFoundError(Exception):
    pass


"""
Class representing a dictionary.

Attributes:
    loaded (bool): Indicates whether the dictionary has been loaded with data.
    data (dict): Dictionary containing word definitions.
    queries (list): List to store queried words and their definitions.

Methods:
    load_dictionary(filepath): Load data into the dictionary from a file.
    query_definition(word=None): Query the dictionary for the definition(s) of a word.
    _query_definition(word): Internal method to query the dictionary for a word's definition(s).
    save_queries_to_file(filepath): Save the queried words and definitions to a text file.
"""


class Dictionary:
    def __init__(self):
        """
        Initializes a Dictionary object with default attributes.
        """
        self.loaded = False
        self.data = {}
        self.queries = []

    def load_dictionary(self, filepath):
        """
        Loads data from a file into the dictionary.

        :param: filepath (str): The path to the file containing dictionary data.

        Raises:
            FileNotFoundError: If the specified file is not found.
            InvalidFileTypeError: If the file extension is not supported.
            JSONDecodeError: If the JSON file has an invalid format.
        """
        try:
            if filepath.endswith(".json"):
                self.data = FileHandler.load_data(filepath, FileExtensions.JSON)
            elif filepath.endswith(".txt"):
                self.data = FileHandler.load_data(filepath, FileExtensions.TXT)
            else:
                raise InvalidFileTypeError(
                    "Invalid file type. Only JSON and TXT files are supported."
                )
            self.loaded = True
            print("Dictionary loaded successfully.")
        except FileNotFoundError as e:
            raise e
        except InvalidFileTypeError as e:
            print(e)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON format in the file: {e}", e.doc, e.pos
            )

    def query_definition(self, word=None):
        """
        Queries the definition of a word.

        :param:word (str, optional): The word to query.

        Raises:
            WordNotFoundError: If the word is not found in the dictionary.
        """
        if not self.loaded:
            print("Dictionary not loaded.")
            return
        last_word = None
        if word:
            self._query_definition(word)
            last_word = word.lower()

        if word:
            self._query_definition(word)
        else:
            while True:
                try:
                    word = input(
                        "Enter a word to look up its definition (type 'logout' to quit): "
                    ).lower()
                    if word == "logout":
                        break  # Exit the loop if the user enters 'exit'

                    # Check if the current word is the same as the last queried word
                    if word.lower() == last_word:
                        print("Word already queried. Skipping...")
                        continue

                    self._query_definition(word)
                    last_word = word.lower()
                except WordNotFoundError as e:
                    print(e)
                except Exception as e:
                    print(f"An error occurred: {e}")

    def _query_definition(self, word):
        """
        Helper method to query the definition of a word.

        :param:word (str): The word to query.

        Raises:
            WordNotFoundError: If the word is not found in the dictionary.
        """
        if word in self.data:
            definitions = self.data[word]
            print(f"Definitions for '{word}':")
            for definition in definitions:
                print("-", definition)
            self.queries.append(
                (word, definitions)
            )  # Save the queried word and its definitions
        else:
            raise WordNotFoundError(f"'{word}' not found in dictionary.")

    def save_queries_to_file(self, filepath):
        """
        Saves queried words and their definitions to a file.

        :param: filepath (str): The path to the file to save queries.
        """
        with open(filepath, "w") as file:
            for word, definitions in self.queries:
                file.write(f"{word}:\n")
                for definition in definitions:
                    file.write(f"- {definition}\n")


def main():
    """
    Main function to execute the dictionary program and unit tests.
    """
    dictionary = Dictionary()
    dictionary.load_dictionary("data.json")
    dictionary.query_definition()
    dictionary.save_queries_to_file("output.txt")


if __name__ == "__main__":
    main()
