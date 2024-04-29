[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13512743&assignment_repo_type=AssignmentRepo)
# Task 1: UML Class Diagrams
Take a look at the UML Class Diagram below This is an extremely simple, bare-bones conceptual model of how a Library program may function. Libraries can search, check out or return books. The first task is to read over and understand a library program based on this class diagram. Remember, commit often!

![](https://cdn.discordapp.com/attachments/1149469347123830804/1156259730122096730/image.png?ex=65145249&is=651300c9&hm=4b971bab8e7cebd47266b4dbcf1544647287abe3ce1e3acb1a8e40410b5cdafd&)

1.	The Library and Book python files have already been written for you. Steps 2-12 explain what has already been written.
1.	Examine both classes and see how they match the UML diagram along with some extra methods.
1.	The `__str__` method should return a string with the book details in a nice formatted manner.
1.	The `check_availability()` method should check the number of copies available and return `True` if there is at least 1 copy available, `False` otherwise
1.	I’ve created a module called `library` and implemented the `Library` class. Note: I’ve imported the `book` module for library to use books.
1.	The `find_book()` method should accept a string title as a parameter and search the list of books for the title and return if it exists. 
    - If the user provides incorrect input, say, due to a spelling error it should return a list of titles similar to the user input and print out a helpful message stating that the book requested could not be found alongside books with similar titles.
    - I recommend taking a look at Python's `difflib` module and its `get_close_matches()` function. (https://docs.python.org/3/library/difflib.html).
1.	The `add_book()` method should accept a book object as a parameter and append it to the `book_list` attribute if it doesn't exist. 
1. The `remove_book()` method should accept a call_number string as a parameter and attempt to delete the item from the book_list. 
1.	The `check_out()` method should accept a call_number string as a parameter and attempt to find the book. If found and available, decrement the number of available copies. It notifies the user if the book is unavailable for check out.
1.	The `return_book()` method should accept a call_number string as a parameter, and increment the number of copies available for that book if it is found.
1.	The `display_available_books()` method should print out the list of books and their details in a nice formatted manner.
1.	There is a `main()` function that creates a new library in `driver.py`. Run the program to test out the functionality and examine the code to fully understand how the entire program works.



## Task 2: Using SOLID Principles and dealing with Dependencies & Coupling
The code provided so far can clearly be improved. Right now, any change in Book will eventually cause changes in the Library. Library is not only dependent, but coupled with Book. We will refactor our code, and modify the class diagram. Let's begin!
1.	Let's refactor our code. We need to split our Library class into Library and Catalogue (Why are we doing this? How does this improve our code?). Implement a Catalogue class will now be responsible for maintaining a list of books. Move all the methods and code related to searching, adding and removing books to this new class.
From this point onwards I won't dictate which class should go into which module. Think about it for a second and feel free to create new modules and restructure your program as you proceed through this lab.
2.	The Library class still needs to be able to access and retrieve book information, but it doesn't need to concern itself with how the search and retrieval occurs. (Which SOLID principle and OOP principles are we working with here?).
    -	Is the book list implemented as a list? A dictionary of tuples? What kind of search algorithm is being used? None of these matter to the Library class. All it needs to do is call the `find_book()` method in the `Catalogue` class.
    -	By refactoring our code this way, we can say that the `Library` is dependent on the `Catalogue` class, but decoupled from the implementation of the book list.
3.	Say the Library underwent a massive upgrade and got access to extra funds through grants! It now maintains DVD's and Scientific Journals in addition to books! (How exciting).
    - This presents an issue. The `Catalogue` is highly dependent and coupled with the `Book` class. We need to use abstraction and interfaces to decouple this unhealthy relationship. How would you do this? Hint: Refer back to our lecture on Inheritance, Interfaces and Abstract Base Classes.
4.	Implement a `Journal` class (Journals have `author`, `issue number`, and a `publisher`), and a `DVD` class (DVD's have a `release date`, and a `region code`). What changes would you need to make to the `Catalogue` class? Would this have any effect on the `Library` Class? Do you need new modules? Do you need to restructure the existing modules?
5.	Let's create a `LibraryItemGenerator` class that is responsible for providing the user with a list of library item types, accepting input and generating that type of item.
6.	Add an `add_item()` function to the `Catalogue` class that is responsible for redirecting the user to the `LibraryItemGenerator` class, creating an item, and then adding it to the catalogue's list of library items. (Your catalogue should maintain a single list of library items. It should not maintain separate lists for books, DVD's and Journals)
7.	Sketch a UML Class diagram of your solution. This doesn't have to be extremely detailed or even generated on your computer. I will accept a scan or photo of a hand drawn one as long as it is legible. Add this as a jpg or png in the same folder as your other python modules and upload it to GitHub. 

# That's It!
That's all for this lab. I hope you had fun writing, architecting and refactoring code. Don't hesitate to ask questions if you still don't understand Dependencies, Coupling, Inheritance or the SOLID principles.
Ensure you push your work to GitHub classroom. I'd like to see sensible git commits comments, and commits must take place at logical points in development.
