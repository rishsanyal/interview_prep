## Create a Producer and Consumer through wait_for and notify_all

import time, random
from threading import Thread, Condition, Semaphore
from queue import Queue, LifoQueue


def producer(w_sem, r_sem, work_list, MAX_LEN):
    """Producer puts in the number in a work_list queue and once it's full,
    the consumer starts popping them and printing them.
    """

    with w_sem:
        global in_num
        print("Starting thread {}".format(in_num))
        # time.sleep(2)
        work_list.put(in_num)
        # condition.notify()

        # work_list[in_num] = in_num
        # wor

        in_num = (in_num + 1) % MAX_LEN

        # print(work_list)
        r_sem.release()


def consumer(w_sem, r_sem, work_list):
    while True:
        with r_sem:
            # condition.wait_for(lambda: work_list.qsize() > 0)
            global out_num, MAX_LEN
            # curr_num = work_list[out_num]
            curr_num = work_list.get(True)
            # work_list[out_num] = None
            out_num = (out_num + 1)# % MAX_LEN
            # print(work_list)

            print("Consumer got {}".format(curr_num))

            time.sleep(0.25)

            w_sem.release()

        # if curr_num == 4:
        #     break

            # print("Consumer condition met!!")

        # if out_num == MAX_LEN:
        #     break

# def consumer_two(condition, work_list):
#     with condition:
#         while True:
#             # condition.wait_for(lambda: work_list.qsize() > 0)
#             curr_num = work_list.pop()

#             print("Consumer 2 got {}".format(curr_num))
#             print(work_list)

#             time.sleep(0.25)

#             # if curr_num == 4:
#             #     break

#             print("Consumer condition met!!")



if __name__ == '__main__':
    cond = Condition()
    threads = []
    MAX_LEN = 4
    q = LifoQueue(MAX_LEN)
    # q = [None for _ in range(MAX_LEN)]

    write_sem = Semaphore(1)
    read_sem = Semaphore(0)

    in_num, out_num = 0, 0

    # t = Thread(target=consumer_two, args=(sem, q))
    # t.start()

    print("Starting producer")
    for i in range(MAX_LEN):
        threads.append(
            Thread(target=producer, args=(write_sem, read_sem, q, MAX_LEN))
        )

    for thread in threads:
        thread.start()

    threads = []
    time.sleep(2)

    print("Starting Consumer")
    print(q)

    for i in range(1):
        threads.append(
            Thread(target=consumer, args=(write_sem, read_sem, q))
        )


    for thread in threads:
        thread.start()

    # threads = []
    # print("Starting producer")
    # for i in range(MAX_LEN):
    #     threads.append(
    #         Thread(target=producer, args=(write_sem, read_sem, q, MAX_LEN))
    #     )

    # for thread in threads:
    #     thread.start()

