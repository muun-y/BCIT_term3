from enum import Enum
import json
from pathlib import Path


"""
Enumeration representing file extensions.

Attributes:
    TXT (str): File extension for text files.
    JSON (str): File extension for JSON files.
"""


class FileExtensions(Enum):
    TXT = "txt"
    JSON = "json"


"""
Custom exception class to handle cases where the file type is not supported.
"""


class InvalidFileTypeError(Exception):
    pass


"""
Class responsible for handling file operations.

Methods:
    load_data(path, file_extension_enum): Load data from a file based on the specified file extension.
    write_lines(path, lines): Write lines of text to a file.
"""


class FileHandler:
    """
    Load data from a file based on the specified file extension.

    Args:
        path (str): The path to the file.
        file_extension_enum (FileExtensions): The file extension enum.

    Returns:
        dict: The loaded data.

    Raises:
        FileNotFoundError: If the file is not found.
        InvalidFileTypeError: If the file type is not supported.
        json.JSONDecodeError: If there is an error decoding JSON data.
    """

    @staticmethod
    def load_data(path, file_extension_enum):
        try:
            # Check if the file exists
            if not Path(path).is_file():
                raise FileNotFoundError("File not found")

            # Determine file type and load data accordingly
            if file_extension_enum == FileExtensions.JSON:
                with open(path, "r") as file:
                    data = json.load(file)
                return data
            elif file_extension_enum == FileExtensions.TXT:
                # Parse text file data into a dictionary
                data = {}
                with open(path, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        parts = line.strip().split(":")
                        if len(parts) >= 2:
                            word = parts[0].strip()
                            definitions = [
                                definition.strip() for definition in parts[1].split(",")
                            ]
                            data[word] = definitions
                return data
            else:
                raise InvalidFileTypeError("Unsupported file type")
        except FileNotFoundError as e:
            raise e
        except json.JSONDecodeError:
            raise

    @staticmethod
    def write_lines(path, lines):
        """
        Write lines of text to a file.

        Args:
            path (str): The path to the file.
            lines (list): The list of lines to write to the file.

        Raises:
            Exception: If there is an error writing to the file.
        """
        try:
            with open(path, "a") as file:
                for line in lines:
                    file.write(line + "\n")
        except Exception as e:
            raise e
        finally:
            print("Check your output file for the results!")
