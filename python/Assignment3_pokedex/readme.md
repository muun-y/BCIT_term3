# **Assignment 3 - An Object-oriented Pokedex**

**Introduction**

You may work in groups of two (2) for this assignment. Create a team or join an existing team on GitHub classroom. Make sure to include both your names and student numbers in comments at the top of driver.py and as a D2L comment when submitting your assignment.

Welcome to the last and final assignment for COMP3522 Object Oriented Programming. I can't believe it's almost the end of the semester!

In the last 12 weeks you all have been exposed to almost every facet of writing complex object oriented programs. You have gone from SOLID Principles, Iterators, generators, to complex concepts such as Multiple Inheritance, Decorators and Factories. As we get into Concurrency this week you will also be learning about AsyncIO , which is a library that lets us execute asynchronous tasks and is the primary focus of this assignment.

In this assignment you will be gaining first hand experience writing asynchronous code that creates HTTP client sessions and queries an endpoint with GET HTTP Requests. To this end we will be implementing `asyncio` tasks and using the `aiohttp` package. We will be creating our very own prototype of Professor Oaks Pokedex. For those of you who are not into Pokémon, a Pokedex is a device that contains all known information about the Pokémon universe. It is a crucial tool in every Pokémon trainers toolbox.

We will be querying the PokéAPI. This is a **REST**ful API. REST stands for **RE**presentational **S**tate **T**ransfer. This is a web application that provides the client (your application) with a **Representation** of the **State** of a requested resource. In simpler words, it provides an instantiated object (attributes only).

For more information about RESTful API, check out this link: https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f 

So back to PokéAPI. This is a RESTful API that can provide information about the pokemon universe. It has different endpoints (URL) that can return data about pokemon, their attack moves, abilities, stats, evolutions etc. The PokéAPI can be found at [https://pokeapi.co/](https://pokeapi.co/).

**Submission Requirements**


1. No late submissions allowed.
2. This is a group assignment. Remember, you may share ideas and discuss the assignment with other groups but do not submit work by anyone else who is not in your group.
3. Submit a short YT video describing how your application works. Highlight any errors or edge cases that are not handled/accounted for. Additionally list any behavior or requirement that is not implemented (if any are left out) as well as any peculiar behaviors or extra functionality.

**Grading**

The **assignment is marked out of 20**. For full marks, you must:

1. Correctly implement the features mentioned above and meet all the requirements set out in this assignment. Handle user input and avoid crashes. - **10 Marks**.
2. Draw a UML Class Diagram that accurately represents your system. **Auto-generated class diagrams will not be accepted** - **3 Marks**
3. Correctly format and comment your code. Follow all the PEP-8 Guidelines and good coding practices. **- 2 Marks**
4. Good coding practices. No unnecessary for loops, use appropriate data types, meaningful identifiers, proper use of SOLID principles where applicable etc. **- 4 Marks**
5. Format your output. Make sure your messages display the correct information in a pleasant, readable manner. You could even use ASCII art if you dare! **- 1 Mark**

Good luck, be creative and have fun!

**Reading the Documentation**

During the course of this assignment you will find yourself regularly accessing its documentation. These can be found at https://pokeapi.co/docs/v2 Before we look at the assignment requirements, let's take a look at what the documentation looks like.

Below we have a screenshot of what the documentation for the Abilities endpoint looks like. (https://pokeapi.co/docs/v2#abilities) ![(https://pokeapi.co/docs/v2#abilities) ](https://media.discordapp.net/attachments/1149469347123830804/1179158889325924442/image.png?ex=6578c44a&is=65664f4a&hm=e54a91d318df935449f15c7d2e5cf9964e19c58226c4c7be7d8847ade3179f1a&=&format=webp&quality=lossless&width=552&height=663)

First off, right at the top this tells us that this is a GET request.

Get requests are simple requests that just retrieve information from a website or service. Unlike Post requests which usually send information and change the state of the data in the web application (e.g.: Sending a username and password to log in). For this assignment we will only be working with GET requests.

This is followed by the endpoint URL suffix. This is the suffix that will appear in your final URL.

**Restful API** : `https://pokeapi.co/api/v2/`

**Abilities Endpoint** : `/api/v2/ability/{id or name}/`

**URL Queried** : `https://pokeapi.co/api/v2/ability/{id or name}/`

Note: the parameters need to be formatted in the final url string. You can even paste this in the web browser to see the response. Try opening https://pokeapi.co/api/v2/ability/magic-guard/ in your browser now.

HINT: Install a browser extension such as JSON Formatter to layout the JSON string in a readable manner. This will help A LOT.

For chrome users this is the link to JSON Formatter: https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en 

This returns a JSON as a response. In our code this will be stored in a `aiohttp.client_reqrep.ClientResponse` object. We can see the structure of the JSON in the table provided below the sample output. The different attributes in the JSON and their types are listed here. These attributes and types are a good look at how objects in your code can be structured. This does NOT have to be a 1-to-1 mapping. You will want to discard attributes that you don't need and perhaps manipulate the information you get to map to the attributes in your class.

**Implementation Requirements**

Our object oriented Pokedex will be a proof of concept prototype. It will not go into the level of detail that the API models, but will depict some basic information.

The following features and functionality should be part of the Pokedex.

**Console Input (and use cases)**

Now, the UI artists and UX Designers are hard at work figuring out the look, feel and flow of the application. This is going to take some time. As good developers you know that you can create the core of the application while they are still working on what the front end looks like. For this assignment you will be creating an application that takes its input from the terminal and can display the output either in the console or print it out to a file as specified by the input.

To achieve this, you need to implement the `argparse` module. You should also read the documentation at https://docs.python.org/3.7/howto/argparse.html . You should do this because:

- It explains everything extremely well and has good examples.
- You will need to refer to the documentation to learn how to use various tools and techniques. This is a skill you need to develop irrespective of the language being used.

You should be able to use the following syntax when running the program and passing parameters from the terminal:

```
python3 driver.py {"pokemon" | "ability" | "move"} {--inputfile "filename.txt" | --inputdata "name or id'} [--expanded] [--output "f] 
```

Let's break this down:

**`python3 driver.py`**

Depending on your system, you will want to use python or python3 followed by the name of the python file to execute. In this case, your driver class and main method will be situated in the driver.py module.


**`{"pokemon" | "ability" | "move"}`**

Curly braces denote a mutually exclusive argument. That is only one of the parameter sets must be selected. In this case it is one argument which must contain one of three values. Any other value for this argument should not be accepted. This is a positional argument, that means it must be provided.

This argument specified the mode that the application will be opened in. It can be one of 3 specific modes, Pokemon, Ability, or Move.

- In the pokemon mode, the input will be an `id` or the `name` of a pokemon. The pokedex will query pokemon information.
- In the ability mode, the input will be an `id` or the `name` of a ability. These are certain effects that pokemon can enable. The pokedex will query the ability information.
- In the move mode, the input will be an `id` or the `name` of a pokemon move. These are the attacks and actions pokemon can take. The pokedex will query the move information.

**`{--inputfile "filename.txt" | --inputdata "name or id'}`**

The curly braces here depict a group of mutually exclusive arguments. There are many different candidate arguments that can be passed in. The user must pass in one of these arguments. They cannot pass in both. I recommend exploring the `add_mutually_exclusive_group` section of the `argparse` documentation (https://docs.python.org/3/library/argparse.html)

As input, the application can take in either a file name (Text file), or a name/id. When providing a file name, the `--inputfile` flag must be provided. The file name must end with a `.txt` extension. If providing just the name or id , then the `–inputdata` flag must be provided. The `id` must be a digit and the `name` a string. This is the second positional argument.

Filenames allow the user to do bulk queries. For example, if executing the app in pokemon mode, then a text file could be a combination of pokemon names and id's, for example:

```
pikachu
Raichu
132
Alakhazam
pidgey
```

Use `asyncio.gather()` to run multiple queries concurrently.

Added Note:
```
If there is an invalid entry when reading in the text file, follow the easier to ask for forgiveness philosophy. Attempt the query and if it fails (you can check the status code of the data returned) then skip it and don't include it in the results (Or replace it with a line saying that the query failed and the input was invalid).

When running a single query (as opposed to many from a file) then if the response from the query is invalid, print an error message either to the console or to the output file (depending on what the user specified in the command line arguments.
```

**`[--expanded]`**

The `--expanded` flag is an optional flag. (Square brackets denote optional parameters).

When this flag is provided, certain attributes are expanded, that is the pokedex will do sub-queries to get more information about a particular attribute. If this flag is not provided, the app will not get the extra information and just print what's provided.

For this prototype, only pokemon queries support the expanded mode. Refer to the pokemon query details below in the document for more information.

**`[--output "filename.txt"]`**

The `--output` flag is optional. If provided, a filename (with a `.txt` extension) must also be provided. and the query result should be printed to the specified text file. If this flag is not provided, then print the result to the console. Be sure to print the file in a nicely formatted, readable manner.

**Get Pokémon Data**

The user should be able to provide the `name` or `id` of a Pokémon and query its information. You want to create a `Pokemon` Class that can store (and ultimately be used to report) the following data:

**Pokemon**

| Name | Type | Expandable | Notes |
| --- | --- | --- | --- |
| Name | String | No | |
| ID | Int | No | |
| Height | Int | No | If printing height, be sure to print it as decimetres. For example, a height value of 100 will be printed as "100 decimetres" |
| Weight | Int | No | If printing weight, be sure to print it as hectograms. For example, a weight value of 100 will be printed as "100 hectograms" |
| Stats | PokemonStat list | Yes | A pokemon query by default returns the name of the stat and it's base value alongside a URL. If the app is run with the `--expanded` flag, then the URL that is provided must also be queried to provide more detailed stat information (see the entry for the stats query below). If the app is not run with the `--expanded` flag then only store the name and the base value. |
| Types | List, string | No | |
| Abilities | PokemonAbility list | Yes | A pokemon query by default returns a list of ability names and corresponding URL's. If the app is run with the `--expanded` flag, then the URL that is provided must also be queried to provide more detailed ability information (see the entry for the ability query below). If the app is not run with the `--expanded` flag then only store the ability name. |
| Moves | PokemonMove list | Yes | A pokemon query by default returns a list of move names, the level at which the move is learnt and corresponding URL's. If the app is run with the `--expanded` flag, then the URL that is provided must also be queried to provide more detailed move information (see the entry for the ability query below). If the app is not run with the `--expanded` flag then only store the move name and the level it is acquired. |

**Get Ability Data**

The user should be able to provide the `name` or `id` of an Ability and query its information. You want to create an `Ability` Class that can store (and ultimately be used to report) the following data:

**Ability**

| Name | Type | Expandable | Notes |
| --- | --- | --- | --- |
| Name | String | No | |
| ID | Int | No | |
| Generation | String | No | |
| Effect | String | No | |
| Effect(Short) | String | No | |
| Pokemon | List, string | No | This would be a simple list of pokemon names. We won't be expanding these. |

**Stats Query (only when querying Pokemon in expanded mode)**

When in expanded mode, the user should be able to query for more details about each stat. You would retrieve the following data:

**Stat**

| Name | Type | Expandable | Notes |
| --- | --- | --- | --- |
| Name | String | No | |
| ID | Int | No | |
| Is Battle Only | bool | No | |

**Get Moves Data**

The user should be able to provide the name or id of an Ability and query its information. You want to create an `MoveClass` that can store (and ultimately be used to report) the following data:

**Move**

| Name | Type | Expandable | Notes |
| --- | --- | --- | --- |
| Name | String | No | |
| ID | Int | No | |
| Generation | String | No | |
| Accuracy | Int | No | |
| PP | Int | No | |
| Power | Int | No | |
| Type | String | No | |
| Damage Class | String | No | |
| Effect (Short) | string | No | |

**Printing a Report**

When a query has finished, it's results must be printed. This "Report" would either be printed to a file, or to the console

(depending on whether the `--output` flag was provided or not).

In both cases the app must print the information in a nicely formatted readable manner. If printing a pokemon query and if the `--expanded` flag was provided, make sure to append Stat, Move and Ability information from the sub-queries as well.

**Facade and Packages**

Its important to group large programs and their modules into packages. These are similar to packages in Java (but not quite the same). A package is simply a directory with modules that are grouped together for some structural reason.

In the assignment you want to create a package called `pokeretriever` . This package will contain all the modules and code required to:

- Create an `aiohttp` session and execute requests
- Parse the JSON and instantiate the appropriate object
- Contains the `Pokemon`, `Ability`, `Move` and `Stat` Classes

I encourage you to read up more on packages at this link: https://realpython.com/python-modules-packages/#python-packages 

The rest of your program will exist outside this package. Implement a facade class that will provide a simplified interface to the `pokeretriever` package. Your program must control access to the package via the interface defined in this facade class.

The facade class should be named appropriately and contain the following method:

`execute_request(request: Request) -> PokedexObject`

- Request is a class that contains all the data gathered by the `argparse` module.
- `PokedexObject` is a base class that defines the `name` and `id` parameter. The `Pokemon` , `Moves` , `Stat` , and `Ability` classes should inherit from this class.
  - This is for returning a single pokemon object return type. The return type will differ when returning a list of PokedexObjects. Feel free to modify this method signature to fit the returned results

- Ensure you push your work to GitHub classroom. I'd like to see sensible git commits comments, and commits must take place at logical points in development.

That's it. Good luck, and have fun!

# FAQ

Is there sample input, output, or script to help testing?

Yes definitely, please check 
https://gist.github.com/nabil828/ffdcfc73563db5871ef070cb1f8ddf4f