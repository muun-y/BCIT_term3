import argparse


class Request:
    """
    Class to handle requests for the PokeAPI.

    Attributes:
        mode (str): The mode that the Pokedex will be opened in. Must be one of 'pokemon', 'ability', or 'move'.
        input_file (str): File to input data from, must end in '.txt'.
        input_data (list): Data to request from the Pokedex, must be int or string.
        is_expanded (bool): Optional argument, runs the Pokedex in expanded mode if True.
        output_file (str): File name to print query result(s) to, must end with '.txt'. If None, output will be printed to the console.
    """

    def __init__(self):
        """
        Initialize a Request object.
        """
        self.mode = None
        self.input_file = None
        self.input_data = None
        self.is_expanded = False
        self.output_file = None
        self.setup_request_commandline()

        if self.input_file:
            self.read_input_file()

    def setup_request_commandline(self):
        """
        Set up command-line arguments for the request.
        """

        parser = argparse.ArgumentParser()
        parser.add_argument("mode",
                            help="The mode that the pokedex will be opened in. Must be one of 'pokemon',"
                                 "'ability' or 'move'.")

        input_group = parser.add_mutually_exclusive_group()
        input_group.add_argument("-f", "--inputfile",
                                 help="File to input data from, must end in '.txt'.")
        input_group.add_argument("-d", "--inputdata",
                                 help="Data to request from the pokedex, must be int or string. Ex. name of a"
                                      "pokemon or id of an ability.")

        parser.add_argument("-e", "--expanded", action="store_true",
                            help="Optional argument, runs pokedex in expanded mode.")
        parser.add_argument("-o", "--output",
                            help="File name to print query result(s) to, must end with '.txt'. Without it,"
                                 "output will be printed to the console.")

        try:
            args = parser.parse_args()
            self.mode = args.mode
            self.input_file = args.inputfile
            self.input_data = args.inputdata
            self.is_expanded = args.expanded
            self.output_file = args.output

        except Exception as e:
            print(f"Argument error! Cannot read arguments.\n{e}")
            quit()

    def read_input_file(self):
        """
        If the --inputfile flag is given, read input text from file.
        :return: None
        """
        with open(self.input_file, mode='r', encoding='utf-8') as file:
            self.input_data = file.readlines()

    def __str__(self):
        return f"Request:\n" \
            f"Mode {self.mode}\n" \
            f"Input file {self.input_file}\n" \
            f"Input data {self.input_data}\n" \
            f"Is expanded? {self.is_expanded}\n" \
            f"Output file {self.output_file}"
