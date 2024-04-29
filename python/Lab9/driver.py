from des import DesKey
import argparse
import abc
import enum


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.
    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
            f", Input file: {self.input_file}, Output: {self.output}, " \
            f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class BaseHandler(abc.ABC):
    """
    Abstract base class for request handlers.
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request: Request) -> (str, bool):
        """
        Handles the request.

        Args:
            request (Request): The request object.

        Returns:
            tuple: A tuple containing a message and a boolean indicating success or failure.
        """
        pass

    def set_handler(self, handler):
        """
        Sets the next handler in the chain.

        Args:
            handler (Handler): The next handler in the chain.
        """
        self.next_handler = handler


class KeyHandler(BaseHandler):
    """
    Handles key validation.
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Validates the key length.

        Args:
            request (Request): The request object.

        Returns:
            tuple: A tuple containing a message and a boolean indicating success or failure.
        """
        if len(request.key) not in [8, 16, 24]:
            return "Invalid key length. Key must be 8, 16, or 24 characters long.", False
        else:
            if not self.next_handler:
                return request.key, True
            return self.next_handler.handle_request(request)


class InputFileHandler(BaseHandler):
    """
    Handles input from a file.
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Reads input data from a file.

        Args:
            request (Request): The request object.

        Returns:
            tuple: A tuple containing a message and a boolean indicating success or failure.
        """
        if request.input_file:
            try:
                with open(request.input_file, 'rb') as file:
                    request.data_input = file.read()
                    if not self.next_handler:
                        return request.data_input, True
                    return self.next_handler.handle_request(request)
            except FileNotFoundError:
                return f"File '{request.input_file}' not found.", False
        else:
            if request.data_input:
                if not self.next_handler:
                    return request.data_input, True
                return self.next_handler.handle_request(request)
            else:
                return "No input file provided.", False


class DataInputHandler(BaseHandler):
    """
    Handles input data.
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Processes input data.

        Args:
            request (Request): The request object.

        Returns:
            tuple: A tuple containing a message and a boolean indicating success or failure.
        """
        if request.data_input:
            if isinstance(request.data_input, str):
                request.data_input = request.data_input.encode('utf-8')

            if not self.next_handler:
                return request.data_input, True
            return self.next_handler.handle_request(request)
        else:
            return "Data input is empty.", False


class EncryptionHandler(BaseHandler):
    """
    Handles encryption of data.
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Encrypts input data.

        Args:
            request (Request): The request object.

        Returns:
            tuple: A tuple containing a message and a boolean indicating success or failure.
        """
        if request.encryption_state == CryptoMode.EN:
            key = request.key
            request.result = DesKey(key.encode()).encrypt(
                request.data_input, padding=True)
            if self.next_handler:
                return self.next_handler.handle_request(request)
            else:
                return request.result, True
        else:
            return "Invalid encryption state for EncryptionHandler.", False


class DecryptionHandler(BaseHandler):
    """
    Handles decryption of data.
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Decrypts input data.

        Args:
            request (Request): The request object.

        Returns:
            tuple: A tuple containing a message and a boolean indicating success or failure.
        """
        if request.encryption_state == CryptoMode.DE:
            try:
                key = request.key
                print()
                request.result = DesKey(key.encode()).decrypt(
                    request.data_input, padding=True)
                if self.next_handler:
                    return self.next_handler.handle_request(request)
                else:
                    return request.result, True
            except Exception as e:
                return f"Decryption failed: {str(e)}", False
        else:
            return "Invalid encryption state for DecryptionHandler.", False


class OutputHandler(BaseHandler):
    """
    Handles the output of the program.
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Manages the output destination.

        Args:
            request (Request): The request object.

        Returns:
            tuple: A tuple containing a message and a boolean indicating success or failure.
        """
        if request.output == 'print':
            if request.encryption_state == CryptoMode.EN:
                print("Encrypted data:", request.result)
            else:
                print("Decrypted data:", request.result)
            return "", True
        elif request.output.endswith(".txt"):
            try:
                with open(request.output, 'wb') as file:
                    if isinstance(request.result, bytes):
                        file.write(request.result)
                    else:
                        file.write(request.result.encode('utf-8'))
                return "", True
            except Exception as e:
                return f"Output handling failed: {str(e)}", False
        elif request.output.endswith(".bin"):
            try:
                with open(request.output, 'wb') as file:
                    file.write(request.result)
                return "", True
            except Exception as e:
                return f"Output handling failed: {str(e)}", False
        else:
            return f"Unsupported output format: {request.output}", False


class Crypto:
    """
    Main class for the Crypto application.
    """

    def __init__(self):
        self.encryption_start_handler = None
        self.decryption_start_handler = None

        # Initialize encryption handler chain
        key_handler_encrypt = KeyHandler()
        input_file_handler_encrypt = InputFileHandler()
        data_input_handler_encrypt = DataInputHandler()
        encryption_handler = EncryptionHandler()
        output_handler_encrypt = OutputHandler()

        key_handler_encrypt.set_handler(input_file_handler_encrypt)
        input_file_handler_encrypt.set_handler(data_input_handler_encrypt)
        data_input_handler_encrypt.set_handler(encryption_handler)
        encryption_handler.set_handler(output_handler_encrypt)

        self.encryption_start_handler = key_handler_encrypt

        # Initialize decryption handler chain
        key_handler_decrypt = KeyHandler()
        input_file_handler_decrypt = InputFileHandler()
        data_input_handler_decrypt = DataInputHandler()
        decryption_handler = DecryptionHandler()
        output_handler_decrypt = OutputHandler()

        key_handler_decrypt.set_handler(input_file_handler_decrypt)
        input_file_handler_decrypt.set_handler(data_input_handler_decrypt)
        data_input_handler_decrypt.set_handler(decryption_handler)
        decryption_handler.set_handler(output_handler_decrypt)

        self.decryption_start_handler = key_handler_decrypt

    def execute_request(self, request: Request):
        """
        Executes the request based on the encryption state.

        Args:
            request (Request): The request object.
        """
        handler = self.encryption_start_handler if request.encryption_state == CryptoMode.EN else self.decryption_start_handler
        result, success = handler.handle_request(request)
        if success:
            print(result)
        else:
            print("An error occurred:", result)


def main(request: Request):
    """
    Main function to execute the Crypto application.

    Args:
        request (Request): The request object.
    """
    crypto = Crypto()
    crypto.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)