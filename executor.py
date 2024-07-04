import heapq
import random
import threading
import time


def fmt_time(t_s):
    return time.strftime('%Y-%m-%d %H:%M:%S %Z', time.gmtime(t_s))


class Task:

    def __init__(self, command, delay, timeunit):
        self.command = command
        self.delay = delay
        self.timeunit = timeunit


class Executor:

    def __init__(self):
        self.queue = []
        heapq.heapify(self.queue)
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.open_threads = []

    def schedule(self, command, delay: int, timeunit):
        """Creates and executes a one-shot action that becomes enabled after
        the given delay."""
        with self.lock:
            heapq.heappush(self.queue, (delay, Task(command, delay, timeunit)))
            self.not_empty.notify()

    def scheduleAtFixedRate(self, command, initialDelay, timeperiod,
                            timeunit):
        """Creates and executes a periodic action that becomes enabled
        first after the given initial delay, and subsequently with the given
        period; that is executions will commence after initialDelay then
        initialDelay+period, then initialDelay + 2 * period, and so on."""
        pass

    def scheduleWithFixedDelay(self, command, initialDelay, delay,
                               timeunit):
        """Creates and executes a periodic action that becomes enabled
        first after the given initial delay, and subsequently with the given
        delay between the termination of one execution and the commencement of
        the next."""
        pass

    def command_exe(self, task):
        print(f"{fmt_time(time.time())} Starting {task.command} - "
              f"{task.timeunit}")
        time.sleep(task.timeunit)
        print(f"{fmt_time(time.time())} Finished {task.command}")

    def execute(self, task):
        print(f"{fmt_time(time.time())} Picked up {task.command}, sleeping "
              f"for {task.delay}")
        time.sleep(task.delay)
        self.command_exe(task)

    def producer(self):
        for i in range(1, 7):
            command = "task" + str(i)
            delay = random.randint(2, 7)
            timeunit = random.randint(2, 2)
            self.schedule(command, delay, timeunit)
            print(f"Added task {command}, {delay}, {timeunit} to the queue")

            time.sleep(0.1)

    def consumer(self):
        while True:
            with self.lock:
                self.not_empty.wait()
                ptask = heapq.heappop(self.queue)
                t = threading.Thread(target=self.execute, args=(ptask[1],))
                t.start()

    def __call__(self, *args, **kwargs):

        print(f"{fmt_time(time.time())}")
        t2 = threading.Thread(target=self.producer, args=(),
                              name="Producer_Thread")
        t1 = threading.Thread(target=self.consumer, args=(),
                              name="Consumer_Thread")

        t1.start()
        t2.start()

        t2.join()
        t1.join()


exec1 = Executor()
exec1()