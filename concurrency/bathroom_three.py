import time
from threading import Thread, Condition, Semaphore, RLock
from queue import Queue
import concurrent.futures
import random

    # def run(self, politician, c_queue):
    #     self.condition.wait_for(lambda: self.getBathroomType() in [politician, None])
    #     self.condition.wait_for(lambda: self.getCurrentSize() >= 0 and self.getCurrentSize() < 3)

    #     self.lock.acquire()
    #     # if not c_queue.empty():
    #     c_queue.get()

    #     print("Waiting here")
    #     sleep_time = 3 #random.randint(1, 3)
    #     print("Inserting politician -> {} with bathroom time -> {}".format(politician, sleep_time))

    #     self.incerementOccupancy(politician)

    #     ## Simulating different bathroom times
    #     time.sleep(sleep_time)

    #     self.decrementOccupancy()
    #     # self.printBathroom()
    #     self.lock.release()

## Producer will enter things into the queues
democrat_queue = Queue()
republican_queue = Queue()

producer_lock = Semaphore(3)
consumer_lock = Semaphore(0)
# condition = Condition()


def producer():
    # time.sleep(random.randint(0, 10))
    producer_lock.acquire()
    customers = ['R', 'D','R', 'D', 'R','R', 'D', 'D', 'D', 'R']

    for politician in customers:
        if politician == 'R':
            republican_queue.put(1)
        else:
            democrat_queue.put(1)

    time.sleep(5)

    democrat_queue.put(None)
    republican_queue.put(None)
    democrat_queue.put(None)
    republican_queue.put(None)
    democrat_queue.put(None)
    republican_queue.put(None)



    consumer_lock.release()

def consumer(i):
    consumer_lock.acquire()
    while True:
        count = 0

        curr_queue = democrat_queue
        curr_party = 'D'

        if curr_queue.empty():
            curr_queue = republican_queue
            curr_party = 'R'

        res = curr_queue.get()

        if res is None:
            break

        print("Printing from consumer num {} with res {}".format(i, res))
        curr_queue.task_done()

    print("Breaking from consumer {}".format(i))
    # bathroom.incerementOccupancy(curr_party)
    # condition.notify_all()

    # time.sleep(random.randint(1, 3))
    # time.sleep(1)

    # bathroom.decrementOccupancy()
    # condition.notify_all()

    producer_lock.release()
    # consumer_lock.release()


class Bathroom(object):
    def __init__(self):
        self.bathroom_occupancy = 0
        self.bathroom_type = None

        self.lock = RLock()

    def printBathroom(self):
        print(self.getCapacity())
        print(self.getBathroomType())

    def getCapacity(self):
        num = 3 - self.bathroom_occupancy
        return num

    def getCurrentSize(self):
        num = self.bathroom_occupancy
        return num

    def incerementOccupancy(self, politician):
        ## Increments Occupancy of bathroom
        with self.lock:
            if self.getCapacity() in [1,2,3] and (self.bathroom_type == politician or self.bathroom_type is None):
                self.bathroom_occupancy += 1
                self.bathroom_type = politician

        return None

    def decrementOccupancy(self):
        ## Decrements occupancy of bathroom
        with self.lock:
            if self.bathroom_occupancy == 0:
                self.setBathroomType(None)
                return

            self.bathroom_occupancy = self.bathroom_occupancy - 1
            if self.bathroom_occupancy == 0:
                self.setBathroomType(None)

    def getBathroomType(self):
        bath_type = self.bathroom_type
        # print(bath_type)
        return bath_type

    def setBathroomType(self, bathroom_type):
        with self.lock:
            self.bathroom_type = bathroom_type
            return



if __name__ == '__main__':
    threads = []

    # customers = ['R', 'D']
    start_time = time.time()

    # bathroom_obj = Bathroom()

    for i in range(1):
        threads.append(
            Thread(target=producer)
        )
        threads[i].start()

    # with concurrent.futures.ThreadPoolExecutor() as manager:
    for i in range(1):
        t = Thread(target=consumer, args=(i, ))
        threads.append(
            t
        )
        t.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    total_time = end_time - start_time

    print(str(total_time))
