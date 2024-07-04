# implement thread-safe stack using a linkedlist.
# Push and pop should be O(1).
# This problem is pretty similar to Design Bounded Blocking Queue.
# Interviewer asked some additional questions prying into my
# knowledge of concurrency primitives.

## This linkedlist needs to scale. Writes need to be correct and reads need to be correct
## It's not like dequeue when we need to block anything

## Is it blocking?
## Make a case for blocking first and then non-blocking


from threading import Semaphore, Thread, Lock
import time
import random

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Stack(object):
    def __init__(self):

        self.head = None

        self.read_lock = Semaphore(0)

        ## How does this Semaphore value influence the number of writes?
        # self.write_lock = Semaphore(5)
        self.mutex = Semaphore(1) #Lock()
        print("Stack initiated")

    def push(self, element):
        time.sleep(random.randint(1,3))
        self.mutex.acquire()

        if not self.head:
            self.head = Node(element)
        else:
            temp_node = Node(element)

            temp = self.head

            self.head = temp_node
            temp_node.next = temp


        self.mutex.release()

    def pop(self):
        res = None
        # self.read_lock.acquire()
        self.mutex.acquire()

        if not self.head:
            res = None
        else:
            res = self.head
            self.head = self.head.next
            res.next = None
            res = res.val

        self.mutex.release()
        print(res)
        return res

    def getTop(self):
        self.mutex.acquire()

        if self.head:
            res = self.head.val
        else:
            res = None

        print(res)

        self.mutex.release()

        return None

    def getAll(self):
        self.mutex.acquire()

        res = []
        temp = self.head

        while temp:
            res.append(
                temp.val
            )

            temp = temp.next

        print(res)

        self.mutex.release()



if __name__ == '__main__':

    threads = []
    s = Stack()


    for i in range(5):
        threads.append(
            Thread(target=s.push, args=(i,))
        )

        # threads.append(
        #     Thread(target=s.getAll)
        # )

    for i in range(3):

        # threads.append(
        #     Thread(target=s.getTop)
        # )

        threads.append(
            Thread(target=s.pop)
        )

        threads.append(
            Thread(target=s.getAll)
        )


    for thread in threads:
        thread.start()


    for thread in threads:
        thread.join()

    # time.sleep(0.25)
