import threading
import time
from city_processor import ISSDataRequest, CityDatabase, CityOverheadTimes
import numpy
import logging
import asyncio

class CityInfoQueue:
    def __init__(self):
        """
        Initialize CityOverheadTimeQueue's data queue.
        """
        self.data_queue = []
        self._access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """
        Append a CityOverheadTimes object to the data queue.
        :param overhead_time: CityOverheadTimes object
        :return: None
        """
        with self._access_queue_lock:
            self.data_queue.append(overhead_time)
            print(f"element added to queue! Queue has {len(self)} elements")

    def get(self) -> CityOverheadTimes:
        """
        Delete the first CityOverheadTimes object in the data queue
        and return the deleted object.
        :return: deleted CityOverheadTimes object
        """
        with self._access_queue_lock:
            if len(self) > 0:
                deleted_element = self.data_queue.pop(0)
                print(f"Element removed from queue! Queue has {len(self)} elements left")
                return deleted_element

    def __len__(self) -> int:
        """
        Return the length of the data queue.
        :return: length of data queue as an int
        """
        return len(self.data_queue)

class ProducerThread(threading.Thread):
    """
    Represents a producer thread that provides data to a common queue.
    """
    id = 1

    def __init__(self, cities: list, queue: CityInfoQueue):
        """
        Initialize Producer Thread details.
        :param cities: a list of City objects
        :param queue: a CityOverheadTimeQueue object
        """
        super().__init__()
        self.cities = cities
        self.queue = queue
        self._id = ProducerThread.id
        ProducerThread.id += 1

    def run(self) -> None:
        """
        Run and adds cities to the queue when the producer thread starts.
        :return: None
        """
        counter = 0
        for city_info in self.cities:
            result = asyncio.run(ISSDataRequest.get_overhead_pass(city_info))
            self.queue.put(result)
            print(f"ISSDataRequest for {city_info.city_name} with params: "
                  f"{{'latitude': {city_info.lat}, 'longitude': {city_info.lng}}}")
            logging.info(f"Producer {self._id} is adding to the queue")
            counter += 1
            if counter % 5 == 0:
                time.sleep(1)

class ConsumerThread(threading.Thread):
    """
    Represents a consumer thread that consumes data from a common queue.
    """
    id = 1

    def __init__(self, queue: CityInfoQueue):
        """
        Initialize Consumer Thread details.
        :param queue: a CityOverheadTimeQueue object
        """
        super().__init__()
        self.queue = queue
        self._id = ConsumerThread.id
        self.data_incoming = True
        ConsumerThread.id += 1

    def run(self):
        """
        Run and remove cities from the queue when the consumer thread starts.
        :return: None
        """
        while self.data_incoming or len(self.queue) > 0:
            if len(self.queue) == 0:
                logging.info(f"Consumer {self._id} is sleeping since queue is empty")
                time.sleep(0.75)
                continue

            item = self.queue.get()
            if item is not None:  
                logging.info(f"Consumer {self._id} is consuming from the queue")
                print("---------")
                print(item)
                print("---------")
            time.sleep(0.5)

def main():
    """
    Drives the program.
    :return: None
    """
    logging.basicConfig(level=logging.INFO, datefmt="%H:%M:%S", format="%(asctime)s: %(message)s")

    start_time = time.time()
    num_threads = 3
    cities_list = numpy.array_split(CityDatabase("city_locations_test.xlsx").city_db, num_threads)
    queue = CityInfoQueue()

    producer_threads = [ProducerThread(cities_list[i], queue) for i in range(num_threads)]
    consumer_thread = ConsumerThread(queue)

    try:
        for producer_thread in producer_threads:
            producer_thread.start()

        consumer_thread.start()

        for producer_thread in producer_threads:
            producer_thread.join()

        consumer_thread.data_incoming = False
        consumer_thread.join()
    except KeyboardInterrupt:
        logging.warning("Program interrupted by user.")
    except Exception as e:
        logging.error(f"Unexpected error in main thread: {str(e)}")

    print("Total duration", time.time() - start_time, " seconds")

if __name__ == '__main__':
    main()
