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


MAX_LEN = 1
q = PriorityQueue(MAX_LEN)

# Creates and executes a one-shot action that becomes enabled after the given delay
class schedule(object):
    def __init__(self, command, delay, unit):
        self.command = command
        self.delay = delay
        self.unit = unit

    def run(self):
        # time.sleep(self.delay)
        # print(self.delay)
        q.put(
            Task(self.command, datetime.datetime.now(), self.unit)
        )

# Creates and executes a periodic action that becomes enabled first after the
# given initial delay, and subsequently with the given period;
# that is executions will commence after initialDelay
# then initialDelay+period, then initialDelay + 2 * period, and so on.
class scheduleAtFixedRate(object):
    def __init__(self, command, initialDelay, period, unit):
        self.command = command
        self.initialDelay = initialDelay
        self.period = period
        self.unit = unit

    def run(self):
        counter = 1
        while True:
            time.sleep(self.initialDelay)
            time.sleep(counter * self.period)
            q.put(
                Task(self.command, datetime.datetime.now(), self.unit)
            )
            counter += 1

# scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)
# Creates and executes a periodic action that becomes enabled first after
# the given initial delay, and subsequently with the given delay
# between the termination of one execution and the commencement of the next.
class scheduleWithFixedDelay(object):
    def __init__(self, command, initialDelay, delay, unit):
        self.command = command
        self.initialDelay = initialDelay
        self.delay = delay
        self.unit = unit

    def run(self):
        while True:
            time.sleep(self.initialDelay)
            time.sleep(self.delay)
            q.put(
                Task(self.command, datetime.datetime.now(), self.unit)
            )

class Task(object):
    def __init__(self, command, priority, size):
        self.command = command
        self.priority = priority
        self.size = size

    def execute(self):
        print("Executing {}".format(str(self)))
        time.sleep(self.size)

    def __str__(self):
        return "Task command -> {}, priority -> {}, task size -> {}".format(
            self.command,
            self.priority,
            self.size
        )

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority


def producer(task, task_args):
    """Producer puts in the number in a work_list queue and once it's full,
    the consumer starts popping them and printing them.
    """
    t = task(*task_args)
    t.run()


def consumer(r_sem):
    while True:
        with r_sem:
            curr_task = q.get(True)
            curr_task.execute()


if __name__ == '__main__':
    threads = []

    read_sem = BoundedSemaphore(4)

    in_num, out_num = 0, 0

    print("Starting producer")
    for i in range(10):
        # task = Task(task_num, task_type, task_args={})
        schedule_args = ['command', 1, 2]
        # command, delay, unit
        threads.append(
            Thread(target=producer, args=(schedule, schedule_args))
        )

    for i in range(1):
        # command, initialDelay, period, unit
        schedule_args = ['command', 1, 1, 1]
        threads.append(
            Thread(target=producer, args=(scheduleAtFixedRate, schedule_args))
        )

    for thread in threads:
        thread.start()

    consumer_threads = []

    start_time = datetime.datetime.now()

    print("Starting Consumer\n\n")

    for i in range(4):
        consumer_threads.append(
            Thread(target=consumer, args=(read_sem, ))
        )

    for thread in consumer_threads:
        thread.start()

    print("Total time -> ", (datetime.datetime.now() - start_time))

