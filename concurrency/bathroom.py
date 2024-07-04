# "question": "* There is single Bathroom to be used in a Voting agency for both
# Democrats(D) and Republicans(R) * This single Bathroom which can accomodate 3
# people at most * each person takes f(N) secs to do his thing. f(N) is a
# function of the person's name and returns varying number * CONDITION:
# At any given time, the bathroom cannot have a mixed set of people i.e.
# * CONDITION: Bathroom can have at most 3 people * these combinations
# aren't allowed (2D, 1R) or (1D,1R) * These are allowed (), (3D), (2D),
# (1R) i.e. pure Republicans or Pure Democrats * While the bathroom is
# occupied people are to wait in a queue * What is the most optimal system
# where you would manage people in this queue, so that * the most eligible
# person instants gets to use the bathroom whenever its has room, based on
# above conditions"

import time
from threading import Thread, Condition
from queue import Queue
import concurrent.futures

DEMOCRAT_BATHROOM_TIME = 1
REPUBLICAN_BATHROOM_TIME = 3

class Bathroom(object):
    def __init__(self):
        self.bathroom_occupancy = 0
        self.bathroom_type = None

        self.democrat_queue = Queue()
        self.republican_queue = Queue()

        self.bathroom_lock = Condition()

        self.threads = []

    def add_to_queue(self, politician):
        if politician == 'R':
            curr_queue = self.republican_queue
            curr_time = REPUBLICAN_BATHROOM_TIME
            ## Once we add someone to the queue,
            ## we create a new blocking thread to get them into the bathroom
        else:
            curr_queue = self.democrat_queue
            curr_time = DEMOCRAT_BATHROOM_TIME

        curr_queue.put(curr_time)

        # curr_thread = Thread(
        #     target=self.__add_to_bathroom
        # )

        # curr_thread.start()
        # curr_thread.join()

        with concurrent.futures.ThreadPoolExecutor() as manager:
            manager.submit(
                self.__add_to_bathroom
            )

        return None

    def __add_to_bathroom(self):
        ## We first get bathroom type
        ## Insert from the bathroom type queue to the bathroom

        curr_queue = self.democrat_queue if not self.democrat_queue.empty() else self.republican_queue
        politician = 'D' if not self.democrat_queue.empty() else 'R'
        curr_time = curr_queue.get()

        with self.bathroom_lock:
            self.bathroom_lock.wait_for(lambda: (self.bathroom_type == politician or self.bathroom_type is None))
            self.bathroom_lock.wait_for(lambda: (self.bathroom_occupancy < 3))

            self.incerementOccupancy(politician)
            self.printBathroom()

            time.sleep(curr_time)

            self.decrementOccupancy()

            # curr_queue.get()
            # print("here")

    def printBathroom(self):
        print(self.getCapacity())
        print(self.getBathroomType())


    def getCapacity(self):
        ## Get available capacity in bathroom
        return 3 - self.bathroom_occupancy

    def getCurrentSize(self):
        ## Get size of bathroom
        return self.bathroom_occupancy

    def incerementOccupancy(self, politician):
        ## Increments Occupancy of bathroom
        self.bathroom_occupancy += 1
        self.bathroom_type = politician
        return None

    def decrementOccupancy(self):
        ## Decrements occupancy of bathroom
        if self.bathroom_occupancy == 0:
            self.setBathroomType(None)
            return

        self.bathroom_occupancy -= 1
        if self.bathroom_occupancy == 0:
            self.setBathroomType(None)

    def getBathroomType(self):
        return self.bathroom_type

    def setBathroomType(self, bathroom_type):
        self.bathroom_type = bathroom_type
        return


if __name__ == '__main__':
    bathroom = Bathroom()

    threads = []

    for i in range(4):
        threads.append(Thread(
            target=bathroom.add_to_queue,
            args=('R')
        ))
        threads.append(Thread(
            target=bathroom.add_to_queue,
            args=('D')
        ))


    # for i in range(2):

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # bathroom.add_to_queue('R')
    # bathroom.add_to_queue('R')
    # bathroom.printBathroom()

    # time.sleep(1)

    # bathroom.add_to_queue('D')
    # bathroom.add_to_queue('D')
    # bathroom.printBathroom()

    # time.sleep(2)
    # bathroom.printBathroom()

