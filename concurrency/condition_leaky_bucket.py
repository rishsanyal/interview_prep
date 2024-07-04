from threading import Condition, Thread
# from queue import Queue, Deque
from collections import deque
from time import sleep
import datetime

class Executor():
    def __init__(self) -> None:
        self.queue = deque()
        self.lock = Condition()
        self.limit = 10

    def add(self):
        if len(self.queue) > self.limit:
            return
        with self.lock:
            self.lock.wait_for(lambda: len(self.queue) <= 10)
            self.queue.append(datetime.datetime.now())
            self.lock.notify_all()

    def remove(self):
        with self.lock:
            self.lock.wait_for(lambda: len(self.queue) > 0, timeout=1)

            if not self.queue:
                return

            print(self.queue.pop())
            self.lock.notify_all()

def leakyBucketAdd(e):
    count = 0
    while True and count < 12:
        sleep(1/3)
        e.add()
        count += 1

def leakyBucketGet(e):
    ctr = 0
    while True and ctr < 5:
        sleep(1 / 10)
        e.remove()

        if len(e.queue) == 0:
            sleep(2)
            ctr += 1
            print(ctr)

if __name__ == "__main__":
    executor = Executor()

    ops = [leakyBucketAdd, leakyBucketAdd, leakyBucketGet]
    threads = []

    for op in ops:
        threads.append([Thread(target=op, args=(executor, )), str(op)])

    for thread in threads:
        thread[0].start()

    for thread in threads:
        # thread[0].start()
        thread[0].join()

    thread_no = 0

    while threads:
        if threads[thread_no][0].is_alive():
            print(threads[thread_no][1])
        else:
            threads.pop(thread_no)

        if len(threads) > 0:
            thread_no = (thread_no + 1) % len(threads)
        else:
            break


    print("all done")

