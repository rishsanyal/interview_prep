# Design and implement a snapshot scheduler
## Priority Task Scheduling - Add Later

## Producer
## Produces Tasks and puts them into the queue
## Call the producer and insert the task in the queue

## Consumer
## Consumes Tasks in a multi-threaded manner
## and executes them

## get the priority of the task

## We use two semaphores
## We want to limit the number of Consumers - BoundedSemaphore

## No need for polling, we insert a task in the queue IF and
## ONLY IF it's ready to be executed. Which means that if it's expted
## Time has come

## Create a Producer and Consumer through wait_for and notify_all

import time, random, datetime
from threading import Thread, Condition, BoundedSemaphore, Lock
from queue import Queue, LifoQueue, PriorityQueue


class Task(object):
    def __init__(self, priority, size):
        self.priority = priority
        self.size = size

    def __str__(self):
        return "Task priority -> {}, task size -> {}".format(
            self.priority,
            self.size
        )

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority


def producer(work_list):
    """Producer puts in the number in a work_list queue and once it's full,
    the consumer starts popping them and printing them.
    """
    task = Task(
        random.randint(1, 3),
        random.randint(2, 4)
    )
    work_list.put(task)
    time.sleep(random.randint(0, 2))


def consumer(r_sem, work_list):
    while not work_list.empty():
        with r_sem:
            curr_task = work_list.get(True)

            print("Consumer got {}".format(curr_task))

            time.sleep(curr_task.size)
            # execute(curr_task)


if __name__ == '__main__':
    cond = Condition()
    threads = []
    MAX_LEN = 20
    q = PriorityQueue(MAX_LEN)
    # q = [None for _ in range(MAX_LEN)]

    write_sem = Lock()
    read_sem = BoundedSemaphore(4)
    # condition = Condition(read_sem)

    in_num, out_num = 0, 0

    print("Starting producer")
    for i in range(MAX_LEN):
        # task = Task(task_num, task_type, task_args={})
        threads.append(
            Thread(target=producer, args=(q, ))
        )

    for thread in threads:
        thread.start()

    threads = []
    time.sleep(2)

    start_time = datetime.datetime.now()

    print("Starting Consumer\n\n")
    # print(q)

    for i in range(4):
        threads.append(
            Thread(target=consumer, args=(read_sem, q))
        )

    for thread in threads:
        thread.start()


    new_producers = []
    print("Starting producer")

    for i in range(MAX_LEN):
        # task = Task(task_num, task_type, task_args={})
        new_producers.append(
            Thread(target=producer, args=(q, ))
        )

    for thread in new_producers:
        thread.start()

    for thread in threads:
        thread.join()



    print("Total time -> ", (datetime.datetime.now() - start_time))

