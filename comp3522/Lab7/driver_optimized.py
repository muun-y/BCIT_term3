"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""

"""
Optimizing Result: 

8066826 function calls in 2.294 seconds >> 107665 function calls in 0.251 seconds

1) is_unique() call count: 2883 times >> delete the function and use set() instead. 
2) Reduce the time complexity of find_unique_words() from O(n^2) to O(n) using word_count dictionary.

"""

import cProfile


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode="r", encoding="utf-8") as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line)
        self.text = stripped_text

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        # remove common punctuation from words
        temp_text = []
        for word in self.text:
            temp_word = word
            for punctuation in self.COMMON_PUNCTUATION:
                temp_word = temp_word.replace(punctuation, "")
            temp_text.append(temp_word)
        self.text = temp_text

    def find_unique_words(self):
        """
        Finds all the unique words in the text.

        This method returns a list of unique words found in the text.
        Words are considered unique if they appear only once in the text.

        :return: A list of all the unique words.
        """

        words_set = set(self.text)
        word_count = {word.lower(): word for word in words_set}

        return list(word_count.values())


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    for word in unique_words:
        print(word)
    print("-" * 50)


if __name__ == "__main__":
    cProfile.run("main()")
