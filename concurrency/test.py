import threading
import queue
import time
import random

class IntegerCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

    def get_count(self):
        with self.lock:
            return self.count

# Shared resource (queue) for producers and consumers
shared_queue = queue.Queue()
integer_counter = IntegerCounter()

# Number of producers and consumers
NUM_PRODUCERS = 2
NUM_CONSUMERS = 3

# Number of integers to be produced
NUM_INTEGERS = 3

# Function for the producer thread
def producer():
    for _ in range(NUM_INTEGERS):
        integer = random.randint(1, 100)  # Generate a random integer
        shared_queue.put(integer)  # Put the integer into the queue
        integer_counter.increment()  # Increment the counter
        print(f"Produced: {integer}")
        time.sleep(1)

# Function for the consumer thread
def consumer():
    while True:
        integer = shared_queue.get()  # Get an integer from the queue
        print(f"Consumed: {integer} by thread {threading.current_thread().name}")
        shared_queue.task_done()  # Indicate that the task is done
        time.sleep(2)

# Create producer threads
producer_threads = []
for i in range(NUM_PRODUCERS):
    t = threading.Thread(target=producer)
    producer_threads.append(t)
    t.start()

# Create consumer threads
consumer_threads = []
for i in range(NUM_CONSUMERS):
    t = threading.Thread(target=consumer)
    consumer_threads.append(t)
    t.start()

# Wait for all producer threads to finish
for t in producer_threads:
    t.join()

# Wait for all consumer threads to finish
for t in consumer_threads:
    t.join()

print("All threads have finished.")
