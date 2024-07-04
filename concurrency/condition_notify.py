import random, time
from threading import Thread, Condition

def task(condition, number):
    print("Thread {} is waiting".format(number))

    with condition:
        condition.wait()
        # condition.notify()

    print("Thread {} is now successful".format(number))


condition = Condition()
threads = []

for i in range(5):
    threads.append(
        Thread(target=task, args=(condition, i))
    )


for i in threads:
    i.start()

time.sleep(3)
# condition.acquire()
# condition.notify_all()
# condition.release()

with condition:
    condition.notify_all()