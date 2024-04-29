# Lab 9 - Chain of Responsibility

**Welcome!**

In today's lab, you will:

1. Implement the Chain of Responsibility Pattern
2. Use the DES (Data Encryption Standard) module to encrypt and decrypt data

## Grading

This lab marked out of 10.

Group members: 2

For full marks this week, you must:

1. (6 points) Implement the Chain of Responsibility Pattern correctly and have the right output
2. (2 points) Follow PEP-8 standards, best practices, OO Design principles, and write good code.
3. (2 points) Draw a UML class diagram to represent your system.

## Requirements

It's time to implement a behavioral pattern. I usually find these to be a lot simpler and easier to understand. In this week's lab we will implement the Chain of Responsibility pattern to create a series of handlers that validate and parse user input followed by either encrypting or decrypting the data according to the options specified.

Install the DES (Data Encryption Standard) package. You will need to install this package via `pip`. If you are using a virtual environment in your PyCharm project install it using the terminal window in PyCharm. To do so enter the following:

```sh
pip3 install des
```

Read through the whole lab before starting. Take a piece of paper and:

- Identify the different classes and their responsibilities
- Identify the different handlers that will be needed to process the request
- Start building your code up from the essential classes to add in extra functionality. That is, get two handlers working first, then add in the third, and so on.

## User Input

This application is meant to be run from the command line. To learn how to do this, open up terminal in MacOS/Linux or cmd in windows. Navigate to the folder with driver.py and type in the following: (depending on your machine you will either need to type in python or python3 )

```sh
python driver.py -h
```

This will bring up a list of positional and optional arguments that can be provided. Many of these arguments will have a short form (e.g `-o` ) and a long form (e.g. `--output` ). Either one can be used.

To correctly encrypt or decrypt data you will need:

- **Properly read and write from/to the file in binary format NOT utf-8**
- data to encrypt or decrypt
- the encryption or *decryption key*. This is a relatively short string that is used by the encryption or decryption algorithm to encode the data.

Here are some examples of possible ways to call the program. Some of the handlers in your program might want to validate the request.

- `python3 driver.py abcd1234 -s "Test Data to be encrypted"` This provides a string to be encrypted with the key `abcd1234`
- `python3 driver.py abcd1234 -f "input\_file.txt"` This provides a text file with the required data that needs to be encrypted with key `abcd1234`
- `python3 driver.py -f "input_file.txt" abcd1234` This is the exact same command as the previous one
- `python3 driver.py abcd1234 --file "input_file.txt"` This is also the exact same command as the previous one. This uses the long form instead
- `python3 driver.py abcd1234 -f "input_file.txt" -m en` This is also the exact same command, but it explicitly sets the mode to encryption
- `python3 driver.py abcd1234 -f "input_file.bin" -m de` This provides a binary file with data that needs to be decrypted with the given key.
- `python3 driver.py abcd1234 -f "input_file.bin" -m de --output print` This is the exact same command as the previous one explicitly stating that the output should be printed to the console.

Open the code and take a look at it. Right now it just prints the request. We use a module called `argparse` to accept input via the command line. This is a very useful tool to know. As a developer you may be asked to write command line tools for other developers. For this lab, you do not need to modify this. I have already set up `argparse` for you.

## Encryption and Decryption

Right, let's get to it.

We will be using the `des` package to encrypt and decrypt a string. DES stands for Data Encryption Standard. It takes a byte string as the key and the data to be encrypted/decrypted.

A byte string here just means that the string is a sequence of bytes. This can easily be achieved by adding the letter `b` as the prefix to a string

```python
byte_string = b"Some string"

my_string = "Some string"

byte_string = my_string.encode() #also converts string to byte string
```

To convert this back to a string we can use the built in `decode` method found in the `str` library.

```python
original_string = byte_string.decode('utf-8')
```

Now that you know what byte strings are, go check out a quick tutorial on how to encrypt or decrypt data using DES. You can find this at: [https://pypi.org/project/des/](https://pypi.org/project/des/)

**Ok, so what do I have to do exactly?**

Implement the Chain of Responsibility Pattern to create handlers that would process the input request. In `driver.py`,
I have included the code to take the command line arguments and assign them to an object of type Request. You will need to:

- Identify all the handlers needed to validate and process the request
  - **Encryption handler** *suggestions*:
    - **KeyHandler**
    #ensure 'key' attribute is valid length (8,16,24)
    - **InputFileHandler**
    #ensure `request.input_file` is non empty, reads data from `request.input_file` into `request.data_input`
    - **DataInputHandler**
    #ensure `request.data_input`` is valid (non empty, is string)
    - **EncryptionHandler**  
    #use `des` library to encrypt data
    - **OutputHandler**  
     #output `request.output` to console or file
      - Unencrypted strings written to a file use `.txt` extension
      - Encrypted data is written to a file use `.bin` extension
  - Decryption Handler *suggestions*
    - **KeyHandler**  
     #ensure 'key' attribute is valid length (8,16,24)
    - **InputFileHandler**  
    #ensure `request.input_file` is non empty, reads data from `request.input_file` into `request.data_input`
    - **DataInputHandler**  
    #ensure `request.data_input`` is valid (non empty, is byte string)
    - **DecryptionHandler**  
     #use des library to decrypt data, handle exceptions
    - **OutputHandler**  
     #output request.output to console or file
      - Unencrypted strings written to a file use `.txt` extension
      - Encrypted data is written to a file use `.bin` extension

- Implement these according to the Chain of Responsibility Pattern.

```python
class Crypto:

    def __init__(self):
        self.encryption_start_handler = None
        self.decryption_start_handler = None

    def execute_request(self, request: Request):
        pass
```

I've also included the stub for the class Crypto which has the following stub methods:

- `__init__(self)`
 This initialization method should set up the two chains of handlers. One for encryption and the other for decryption. It should store the reference to the first handler of each chain in `self.encryption_start_handler` and `self.decryption_start_handler` respectively.
- `execute_request(self, request: Request)` This method accepts a request and starts executing the first handler in the appropriate chain.

Include an `Enum` called `CryptoMode` which defines two modes that the application can run in. An `EN` (Encryption) mode and a `DE` (Decryption Mode). This enum is used by the included Crypto class in the `execute_request` method to determine whether to run the encryption, or decryption handlers.

After implementing the handlers and connecting it to the existing code, test your program to ensure that it can handle encrypting and decrypting strings in different scenarios. For example:

1. Encrypting a string from console or file and outputting to the screen or file
2. Decrypting a string from console or file and outputting to the screen or file

I've also included a **test.cmd** script that can be run on windows via the command prompt. This test script will quickly run your code in a variety of scenarios. Feel free to modify this file with new test cases. To run the script, enter the terminal, navigate to the lab folder, and type "test" and Enter.

Ensure you push your work to github classroom. I'd like to see sensible git commits comments, and commits must take place at logical points in development.
