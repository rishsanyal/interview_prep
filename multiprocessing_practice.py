from multiprocessing import Process, Lock
import time

def add(a, b):
    try:
        print("Adding {a}, {b} -> ", a+b)
        time.sleep(5)
    except Exception as e:
        print(e)

def sub(a, b):
    try:
        print("Subtracting {a}, {b} -> ", a-b)
        time.sleep(10)
    except Exception as e:
        print(e)

def task(lock, identifier, value):
    # acquire the lock
    lock.acquire()
    print(f'>process {identifier} got the lock, sleeping for {value}')
    time.sleep(value)
    lock.release()


    lock.acquire()
    print(f'>process {identifier} got the lock again, sleeping for {value}')
    time.sleep(value)
    lock.release()




def main():
    a = 1
    b = 2

    # add_process = Process(target=add, args=(a, b))
    # sub_process = Process(target=sub, args=(a, b))

    # ## Starts the processes
    # add_process.start()
    # sub_process.start()


    # ## Waits on the processes to finish
    # add_process.join()

    # print("waiting on sub")
    # sub_process.join()

    lock = Lock()
    process_1 = Process(target=task, args=(lock, 1, 5))
    process_2 = Process(target=task, args=(lock, 2, 2))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()


if __name__ == '__main__':
    main()