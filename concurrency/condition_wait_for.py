import random, time
from threading import Thread, Condition

from queue import Queue
# from multiprocessing import Process, Condition, Queue

def task(condition, work_list, number):
    print("Thread {} is waiting".format(number))

    with condition:
        work_list.put(number)
        condition.notify_all()

    print("Thread {} is now successful".format(number))


if __name__ == '__main__':
    condition = Condition()
    threads = []
    work_l = Queue(maxsize=5)

    for i in range(5):
        p = Thread(target=task, args=(condition,work_l, i))
        p.start()
        threads.append(p)

    for thread in threads:
        thread.join()


    # for i in threads:
    #     i.start()

    # time.sleep(3)

    # condition.acquire()
    # condition.notify_all()
    # condition.release()

    with condition:
        condition.wait_for(work_l.full)
        print("Condition Met!")