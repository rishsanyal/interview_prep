# Implement a thread-safe bounded blocking queue that has the following methods:

#     BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
#     void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
#     int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
#     int size() Returns the number of elements currently in the queue.

from threading import Condition, Thread
from queue import Queue

class BoundedBlockingQueue():

    def __init__(self, max_cap):
        self.max_cap = max_cap
        # self.cal = 0
        self.queue = []
        self.lock = Condition()

    def enqueue(self, element):
        with self.lock:
            self.lock.wait_for(lambda: len(self.queue) < self.max_cap)
            print("Inserting {}".format(element))
            self.queue.append(element)
            self.lock.notify_all()

    def dequeue(self):
        res = None

        with self.lock:
            print("Dequeue cond {}".format(len(self.queue) > 0))
            self.lock.wait_for(lambda: len(self.queue) > 0)
            res = self.queue.pop(0)
            print("Got {} from queue".format(res))
            self.lock.notify_all()

        return res


    def size(self):
        curr_cap = 0
        with self.lock:
            curr_cap = len(self.queue)
            print(curr_cap)

        return curr_cap



if __name__ == '__main__':
    # queue_obj = BoundedBlockingQueue(10)

    # threads = []



    # for i in range(12):
    #     threads.append(
    #         Thread(target=queue_obj.enqueue, args=(i, ))
    #     )

    # for thread in threads:
    #     thread.start()

    # threads = []

    # for i in range(12):
    #     threads.append(
    #         Thread(target=queue_obj.dequeue)
    #     )

    # for thread in threads:
    #     thread.start()

    cmd_list = ["BoundedBlockingQueue","enqueue","dequeue", "enqueue", "enqueue","enqueue", "dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue", "size"]
    cmd_value_list = [[10],[1],[], [2],[3],[10], [],[],[5],[6],[7],[8],[], []]
    threads = []

    queue_obj = None

    while cmd_list:
        cmd = cmd_list.pop(0)
        cmd_val = cmd_value_list.pop(0)
        if cmd == "BoundedBlockingQueue":
            queue_obj = BoundedBlockingQueue(cmd_val[0])
        elif cmd == "enqueue":
            threads.append(
                Thread(target=queue_obj.enqueue, args=(cmd_val[0], ))
            )
        elif cmd == "dequeue":
            threads.append(
                Thread(target=queue_obj.dequeue)
            )
        elif cmd == "size":
            threads.append(
                Thread(target=queue_obj.size)
            )

    for thread in threads:
        thread.start()




    # queue = BoundedBlockingQueue(2)    # initialize the queue with capacity = 2.

    # queue.enqueue(1)    # The producer thread enqueues 1 to the queue.
    # queue.enqueue(1)    # The producer thread enqueues 1 to the queue.
    # # queue.enqueue(1)    # The producer thread enqueues 1 to the queue.
    # queue.dequeue()     # The consumer thread calls dequeue and returns 1 from the queue.
    # queue.dequeue()     # Since the queue is empty, the consumer thread is blocked.
    # queue.enqueue(0)    # The producer thread enqueues 0 to the queue. The consumer thread is unblocked and returns 0 from the queue.
    # queue.enqueue(2)    # The producer thread enqueues 2 to the queue.
    # queue.dequeue()     # Since the queue is empty, the consumer thread is blocked.
    # # queue.dequeue()     # Since the queue is empty, the consumer thread is blocked.
    # queue.enqueue(3)    # The producer thread enqueues 3 to the queue.
    # queue.enqueue(4)    # The producer thread is blocked because the queue's capacity (2) is reached.
    # queue.dequeue()     # The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
    # print(queue.size())        # 2 elements remaining in the queue. size() is always called at the end of each test case.


    ## This should not block