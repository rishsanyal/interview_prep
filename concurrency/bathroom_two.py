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
from threading import Thread, Condition, Semaphore, RLock
from queue import Queue
import concurrent.futures
import random

# def Producer
## Producer will enter things into the queues
democrat_queue = Queue()
republican_queue = Queue()

# class Producer():
#     # def __init__(self):
#     #     self.lock = Semaphore(1)

def producer(politician):
    ## Insert into queue

    # time.sleep(random.randint(0, 10))
    if politician == 'R':
        republican_queue.put(1)
    else:
        democrat_queue.put(1)

def consumer(in_manager):
    curr_type = 'D'
    bathroom_obj = Bathroom()
    # futures = []
    count = 0

    # while True:
    ## Goes between the two queues
    if curr_type == 'D':
        curr_queue = democrat_queue
    else:
        curr_queue = republican_queue

    if democrat_queue.empty() and republican_queue.empty():
        count += 1
        time.sleep(1)
        # continue

    if count >= 3:
        print("Breaking")
        # break

    if curr_queue.empty():
        if curr_type == 'D':
            curr_type = 'R'
        else:
            curr_type = 'D'
    else:
        in_manager.submit(bathroom_obj.run, curr_type, curr_queue)

    # with concurrent.futures.ThreadPoolExecutor() as manager:
    #     print("Executing")
    #     futures.append(
    #         manager.submit(bathroom_obj.run, curr_type)
    #     )


# def Consumer

class Bathroom(object):
    def __init__(self):
        self.bathroom_occupancy = 0
        self.bathroom_type = None

        # self.run_lock = Semaphore(3)
        self.lock = RLock() #Semaphore(3)
        self.condition = Condition()

    def run(self, politician, c_queue):
        sleep_time = 3 #random.randint(1, 3)
        self.incerementOccupancy(politician)

        print("Waiting here")
        c_queue.get()

        self.printBathroom()


        ## Simulating different bathroom times
        # time.sleep(sleep_time)

        # self.decrementOccupancy()
        # print("Decremeter")
        # self.printBathroom()
        # self.run_lock.release()


    def printBathroom(self):
        print(self.getCapacity())
        print(self.getBathroomType())

    def getCapacity(self):
        ## Get available capacity in bathroom
        # self.lock.acquire()
        num = 3 - self.bathroom_occupancy
        # self.lock.release()

        return num

    def getCurrentSize(self):
        ## Get size of bathroom
        # self.lock.acquire()
        num = self.bathroom_occupancy
        # self.lock.release()

        return num

    def incerementOccupancy(self, politician):
        # self.condition.wait_for(lambda: self.getCurrentSize() >= 0 and self.getCurrentSize() < 3)
        # self.condition.wait_for(lambda: self.getBathroomType() in [politician, None])
        # print("Inserting politician -> {} with bathroom time -> {}".format(politician, sleep_time))

        ## Increments Occupancy of bathroom
        with self.lock:
            print("Waiting here with", politician)
            self.bathroom_occupancy += 1
            self.bathroom_type = politician

            # self.condition.notify_all()
        # self.lock.release()


    def decrementOccupancy(self):
        ## Decrements occupancy of bathroom

        with self.lock:
            if self.bathroom_occupancy == 0:
                self.setBathroomType(None)
                return

            self.bathroom_occupancy = self.bathroom_occupancy - 1
            if self.bathroom_occupancy == 0:
                self.setBathroomType(None)

            # self.condition.notify_all()
        # self.lock.release()

    def getBathroomType(self):
        # self.lock.acquire()
        bath_type = self.bathroom_type
        # self.lock.release()
        # self.condition.notify_all()
        return bath_type

    def setBathroomType(self, bathroom_type):
        # self.lock.acquire()
        self.bathroom_type = bathroom_type
        self.condition.notify_all()
        # self.lock.release()
        return


if __name__ == '__main__':
    threads = []

    customers = ['R', 'D','R', 'D', 'R','R', 'D', 'D', 'D', 'R']
    # customers = ['R']

    start_time = time.time()

    for i, val in enumerate(customers):
        threads.append(
            Thread(target=producer, args=(val, ))
        )
        threads[i].start()


    with concurrent.futures.ThreadPoolExecutor() as manager:
        for i, val in enumerate(customers):
            t = Thread(target=consumer, args=(manager, ))
            threads.append(t)
            t.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    total_time = end_time - start_time

    print(str(total_time))




    # for i in range(1):
    #     threads.append(
    #         Thread(target=consumer)
    #     )

    #     threads[0].start()

    # for i, val in enumerate(customers):
    #     threads.append(
    #         Thread(target=producer, args=(val))
    #     )
    #     threads[i].start()






    # p.insert('D')
    # # c.consumer()

    # p.insert('R')

