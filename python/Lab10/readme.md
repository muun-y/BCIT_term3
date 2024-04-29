# **Lab 10 - Looking Down from Space**

# Welcome

In today's lab, you will:

1. Get first hand experience implementing threads and concurrency
2. Learn how to use Locks to ensure Mutual Exclusion when accessing resources shared across threads.
3. Get a chance to work with a web API service that provides data about the International Space Station.

# Grading

This lab will be marked out of 10.

For full marks this week, you must:

1. (6 points) Implement the Produce-Consumer problem correctly.
2. (4 points) Follow PEP-8 standards, best practices, OO Design principles, and write good code.

# Requirements

In today's lab we are going to tackle the famous producer-consumer problem. In this problem, one or more threads are known as **producers** , that is they provide data to a common **buffer** (in our case, a **queue** )

And as you may expect there are one or more threads knowns as consumers, who read and remove data from this common buffer and do something with it

This is an extremely simple problem and a great way to get your hands dirty with writing multithreaded code.

If you haven't done so yet, install the requests module.

This is very IMPORTANT. Read through the whole document before starting to code. This will help you understand the problem and what you need to do.

In today's lab we will be getting data from the **Open Notify**  **Project**. The project specified a few **endpoints** (read: URL's or addresses) that each define a differentAPI.

Remember, an API is known as an **Application Programming Interface** , this is an interface that defines ways to interact with one or more behaviors. In this case, these are **Web APIs** that allow us as developer to send requests to a Server and receive a response

Try entering the following in your browser. This shows time zone information about Vancouver

[https://api.wheretheiss.at/v1/coordinates/49.2734,-123.1216](https://api.wheretheiss.at/v1/coordinates/49.2734,-123.1216)

Visit this site for more information about the API: [https://wheretheiss.at/w/developer](https://wheretheiss.at/w/developer)

We will be accessing the "Where the ISS at?" REST API. What this means is that we can provide the endpoint with a location (latitude and longitude) and find out information (`latitude, longitude, timezone_id, offset, country_code, map_url`) about that city. I don't know about you, but I thought this was really cool and interesting.

In this lab, you will be loading data about Canadian cities (their name, latitude and longitude) from the **city_locations.xlsx** file using pandas (NOTE: This is not an exhaustive list). The code to read and convert this data into usable objects has already been done for you.

## Step 1: Get data from the endpoint

The first thing clone the repo containing the following:

- **city_locations.xlsx**
- **city_locations_test.xlsx**
- **city_processing.py**

Go through the file and try running it. I have provided all the data structures and code you need to read the excel file and parse it into a database of cities. Let's break down the code shall we:

- `jprint`

This is a function to help you debug the response you will be getting from the endpoint. This will make more sense as you read the referenced tutorial and start coding.

- `City`

This data structure represents a single city. It stores the name, latitude and longitude of the city.

- `CityDatabase`

This is the "Database" of cities that we will be processing .This class will read an excel file and parse it into a list of **City** objects

- `CityInfo`

This is a data structure that represents all the information about a city

- `ISSDataRequest`

This class acts as a **Façade** to the **Open Notify ISS Pass API**. This API accepts a latitude and a longitude as its parameters and sends data about the next times the ISS will pass over the provided location

Open up <https://www.dataquest.io/blog/python-api-tutorial/>  and read the tutorial on how to use **GET Requests** to get data from an endpoint. This is not difficult at all (especially since we don't need to provide a key and get authenticated). Once you have done this fill in the missing code in the **ISSDataRequest** class to query the endpoint for a response. Use the JSON response to create and return a **CityInfo** object for the specified city.

Write some code to test out and ensure that your code works. Use the **city_locations_test.xlsx** file for test data and print out the corresponding **CityInfo** objects for each city.

You are not allowed to modify any of the provided code in city_processor.py except for `get_overhead_pass` method in the ISSDataRequest class. Your code should not need to change any of the other existing classes to work

## Step 2: Creating our Buffer

All code from this point onwards should be in **driver.py**.

The first step in our producer-consumer problem is to create a buffer that will hold the calculated **CityInfo** objects. We will use a **Queue** for this. Create a **CityInfoQueue** class with the following methods.

- **def _init_(self):**

Instantiates an attribute called **data_queue** as an empty list

```
Python provides a built-in queue class that is thread safe. However, for this lab, we will be implementing our own queue class to get some practice with threads and locks. 
```

- **def put(self, city_info: city_processor.CityInfo) -\> None:**

This method is responsible for adding to the queue. Accept a city_info parameter and append it to the data_queue list.

- **def get(self) -\> city_processor.CityInfo:**

This method is responsible for removing an element from a Queue. Remember a queue is a FIFO data structure, that is it is First In First Out. Each call to this method should return the element at index 0 and delete it from the list. Use the **del** keyword to delete the element as this will also automatically move all the other elements so there will be no empty spaces.

- **def _len_(self) -\> int:**

This magic method should return the length of the **data_queue**

Write some code in **main** to test out this data structure. Make sure this is working as expected before proceeding

## Step 3: Creating a Producer and a Consumer Thread

We now need to create 2 classes that inherit from the **Thread** class found in the **threading** module. Import the threading module and create the following classes:

1. Producer Thread

The ProducerThread class inherits from the Thread class. It has the following methods:

- **def _init_(self, cities:list, queue: CityInfoQueue):**

This method initializes the class with a list of **City** Objects as well as a **CityInfoQueue**

- **def run(self) -\> None:**
This method executes when the thread starts. It should loop over each **City** and pass it to the **ISSDataRequest.get_overhead_pass()** method. It then proceeds to add the city to the queue. After reading in **5** cities, the thread should sleep for 1 second.

At this point, write some code in the main method to create, start, and join a ProducerThread and ensure this thread works as intended.

1. ConsumerThread

The ConsumerThread is responsible for consuming data from the queue and printing it out to the console. It has the following methods:

- **def _init_(self, queue: CityInfoQueue):**

Initializes the ConsumerThread with the same queue as the one the producer has. It also implements a **data_incoming** Boolean attribute that is set to **True**. This attribute should change to **False** after the producer threads have joined the main thread and finished processing all the cities.

- **def run(self) -\> None:**

While **data_incoming** is true OR the length of the queue is \> 0, this method should get an item from the queue and print it to the console and then sleep for **0.5** seconds. If the queue is empty while processing, put the thread to sleep for **0.75** seconds.

Now write some more code in the main method to create a consumer thread and make sure it works as intended

## Step 4: Adding locks

Right now we are accessing a shared resource (the buffer) with 2 threads. Since the operating system can interrupt a thread and switch between them randomly, the queue may not be in sync. To ensure that we are accessing shared variables and resources safely we need to implement **Locks**.

Locks allow us to define areas of code for **Mutual Exclusion**. This means that only one thread can acquire the lock and access that block of code at a time. Mutual exclusion ensures that only one thread is modifying the queue at any given time. This avoid Race Conditions.

Race conditions are what happens when Locks are not implemented. These are situations where the order in which instructions are executed gets mixed up due to multiple switching threads and this causes errors.

Go read the **W12 Lab Race Condition Slides** on D2L to understand how locks work. I have also included some sample code (thread_race_condition_fixed_example.py) to show you how to implement them. It's really easy!

Add an attribute to our **CityInfoQueue** called **access_queue_lock** in its **_init_** method. Use this lock to control access to the code in the **put** and **get** methods. Test and run the code again to ensure it works as expected

You may want to use **city_locations_test.xlsx** for testing so you don't spend a lot of time waiting to process 100 something cities. You can add more cities to this excel sheet to gradually increase the amount of cities as well.

Step 5: Adding more producers

The final step is to create 2 more producer threads. Split the cities from the city database across these three threads and start them. This should speed up your code and requests significantly.

NOTE: You don't need to add a lock to the ISSDataRequest's get_overhead_pass method since it only works with local variables. Each thread keeps its own copy of local variables.

- Ensure you push your work to GitHub classroom. I'd like to see sensible git commits comments, and commits must take place at logical points in development.

That's it for this lab!

**Sample output** when running the completed program with the included city_location_text.xlsx excel file. There are **3 producer** and **2 consumer** threads:

```
ISSDataRequest for Vancouver with params: {'latitude': 49.2734, 'longitude': -123.1216}

ISSDataRequest for Camrose with params: {'latitude': 53.0167, 'longitude': -112.8166}

ISSDataRequest for Revelstoke with params: {'latitude': 51.0005, 'longitude': -118.1833}

11:52:47: Consumer 1 is sleeping since queue is empty

11:52:47: Consumer 2 is sleeping since queue is empty

element added to queue! Queue has 1 elements

11:52:47: Producer 3 is adding to the queue

ISSDataRequest for Meadow Lake with params: {'latitude': 54.1301, 'longitude': -108.4347}

element added to queue! Queue has 2 elements

11:52:47: Producer 1 is adding to the queueelement added to queue! Queue has 3 elements

ISSDataRequest for Yellowknife with params: {'latitude': 62.442, 'longitude': -114.397}

11:52:47: Producer 2 is adding to the queue

ISSDataRequest for Campbell River with params: {'latitude': 50.0171, 'longitude': -125.25}

element added to queue! Queue has 4 elements

11:52:47: Producer 1 is adding to the queue

element added to queue! Queue has 5 elements

11:52:47: Producer 3 is adding to the queue

ISSDataRequest for Montreal with params: {'latitude': 45.5, 'longitude': -73.5833}

element added to queue! Queue has 6 elements

11:52:47: Producer 2 is adding to the queue

element removed from queue! Queue has 5 elements left

11:52:48: Consumer 1 is consuming from the queue

---------element removed from queue! Queue has 4 elements left

11:52:48: Consumer 2 is consuming from the queue

---------

latitude: 49.2734

longitude: -123.1216

timezone_id: America/Vancouver

offset: -8

country_code: CA

map_url: https://maps.google.com/maps?q=49.2734,-123.1216&z=4

---------

latitude: 51.0005

longitude: -118.1833

timezone_id: America/Vancouver

offset: -8

country_code: CA

map_url: https://maps.google.com/maps?q=51.0005,-118.1833&z=4

---------

element added to queue! Queue has 5 elements

11:52:48: Producer 3 is adding to the queue

element removed from queue! Queue has 4 elements left

11:52:48: Consumer 2 is consuming from the queue

element removed from queue! Queue has 3 elements left

11:52:48: Consumer 1 is consuming from the queue

------------------

latitude: 53.0167

longitude: -112.8166

timezone_id: America/Edmonton

offset: -7

country_code: CA

map_url: https://maps.google.com/maps?q=53.0167,-112.8166&z=4

latitude: 62.442

longitude: -114.397

timezone_id: America/Yellowknife

offset: -7

country_code: CA

map_url: https://maps.google.com/maps?q=62.442,-114.397&z=4

---------

---------

element removed from queue! Queue has 2 elements left

11:52:49: Consumer 1 is consuming from the queueelement removed from queue! Queue has 1 elements left

---------

11:52:49: Consumer 2 is consuming from the queuelatitude: 54.1301

longitude: -108.4347

timezone_id: America/Swift_Current

offset: -6

country_code: CA

map_url: https://maps.google.com/maps?q=54.1301,-108.4347&z=4

---------

---------

latitude: 50.0171

longitude: -125.25

timezone_id: America/Vancouver

offset: -8

country_code: CA

map_url: https://maps.google.com/maps?q=50.0171,-125.25&z=4

---------

element removed from queue! Queue has 0 elements left

11:52:49: Consumer 2 is consuming from the queue

---------

latitude: 45.5

longitude: -73.5833

timezone_id: America/Toronto

offset: -5

country_code: CA

map_url: https://maps.google.com/maps?q=45.5,-73.5833&z=4

---------

Total duration 2.7602810859680176 seconds

Process finished with exit code 0

```
