import unittest
import json
from io import StringIO
from unittest.mock import patch
from driver import Dictionary, WordNotFoundError
from file_handler import (
    FileHandler,
    FileExtensions,
    InvalidFileTypeError,
)

"""
This class contains unit tests for the Dictionary class and related functionalities.

Test cases are provided for:
- Loading data into a dictionary from JSON and TXT files.
- Handling file not found and invalid file type errors gracefully.
- Writing data to a text file.
- Querying definitions for words, including cases where the word is found or not found, and case insensitivity.
"""


class TestDictionary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up class method to load data from files before running test cases.
        """

        with open("data.json", "r") as file:
            cls.json_data = json.load(file)

        with open("data.txt", "r") as file:
            cls.txt_data = {}
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(":")
                if len(parts) >= 2:
                    word = parts[0].strip()
                    definitions = [
                        definition.strip() for definition in parts[1].split(",")
                    ]
                cls.txt_data[word] = definitions

    def test_load_dictionary_correct_input(self):
        """
        Test loading data into a dictionary with correct input.
        """

        with patch.object(FileHandler, "load_data", return_value=self.json_data):
            dictionary = Dictionary()
            dictionary.load_dictionary("data.json")
            self.assertTrue(dictionary.loaded)
            self.assertEqual(dictionary.data, self.json_data)

        with patch.object(FileHandler, "load_data", return_value=self.txt_data):
            dictionary = Dictionary()
            dictionary.load_dictionary("data.txt")
            self.assertTrue(dictionary.loaded)
            self.assertEqual(dictionary.data, self.txt_data)

    def test_load_dictionary_file_not_found(self):
        """
        Test loading data into a dictionary that does not exist (file not found).
        """
        with self.assertRaises(FileNotFoundError):
            dictionary = Dictionary()
            dictionary.load_dictionary("data1.json")

    def test_load_invalid_type_file(self):
        """
        Test loading data into a dictionary with an invalid file type.
        """
        # Arrange
        file_handler = FileHandler()
        invalid_file_path = "data.xml"

        # Act & Assert
        with self.assertRaises(InvalidFileTypeError) as context:
            file_handler.load_data(invalid_file_path, FileExtensions)

        # Assert
        self.assertEqual(str(context.exception), "Unsupported file type")

    def test_load_dictionary_invalid_json(self):
        """
        Test loading data into a dictionary with incorrect input (invalid JSON format).
        """
        with self.assertRaises(json.JSONDecodeError):
            dictionary = Dictionary()
            dictionary.load_dictionary("no_data.json")

    def test_write_lines_with_json_data(self):
        """
        Test writing data to a text file with JSON data.
        """

        with open("data.json", "r") as file:
            json_data = json.load(file)

        # Write JSON data to a text file
        with open("test_output.json", "w") as file:
            json.dump(json_data, file)

        # Check if the data was written correctly to the file
        with open("test_output.json", "r") as file:
            written_data = json.load(file)
            self.assertEqual(written_data, json_data)

    def test_load_txt_file(self):
        """
        Test loading text data from a file.
        """
        with open("data.txt", "r") as file:
            txt_data = file.read()
            expected_data = txt_data

        # Write JSON data to a text file
        with open("test_output.txt", "w") as file:
            json.dump(txt_data, file)

        # Check if the data was loaded correctly from the file
        with open("test_output.txt", "r") as file:
            written_data = json.load(file)
            self.assertEqual(written_data, expected_data)

    def test_query_definition_word_found(self):
        """
        Test querying definition for a word that is found in the dictionary.
        """
        dictionary = Dictionary()
        dictionary.data = self.json_data

        with patch("builtins.input", side_effect=["adhesive"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                dictionary._query_definition("adhesive")
                expected_output = "Definitions for 'adhesive':\n- Substance used for sticking objects together.\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_query_definition_word_not_found(self):
        """
        Test querying definition for a word that is not found in the dictionary.
        """
        dictionary = Dictionary()
        dictionary.data = self.json_data

        with patch("builtins.input", side_effect=["nonexistent"]):
            with self.assertRaises(WordNotFoundError):
                dictionary._query_definition("nonexistent")

    def test_query_definition_case_insensitive(self):
        """
        Test querying definition with case insensitive input.
        """
        dictionary = Dictionary()
        dictionary.data = self.json_data

        with patch("builtins.input", side_effect=["aDheSive"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                dictionary._query_definition("adhesive")
                expected_output = "Definitions for 'adhesive':\n- Substance used for sticking objects together.\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
