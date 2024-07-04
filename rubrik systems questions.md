"question": "* There is single Bathroom to be used in a Voting agency for both Democrats(D) and Republicans(R) * This single Bathroom which can accomodate 3 people at most * each person takes f(N) secs to do his thing. f(N) is a function of the person's name and returns varying number * CONDITION: At any given time, the bathroom cannot have a mixed set of people i.e. * CONDITION: Bathroom can have at most 3 people * these combinations aren't allowed (2D, 1R) or (1D,1R) * These are allowed (), (3D), (2D), (1R) i.e. pure Republicans or Pure Democrats * While the bathroom is occupied people are to wait in a queue * What is the most optimal system where you would manage people in this queue, so that * the most eligible person instants gets to use the bathroom whenever its has room, based on above conditions"

"answer":"* Solution: * Bathroom is a single reference object with functions to getCapacity(), getCurrentSize(), incerementOccupancy(), decrementOccupancy(), getBathroomType(), setBathroomType() * There are 2 Blocking queues (self implemented) one for Republicans and one for Democrats * Every new person added in the queue represents a new task to be executed by a thread * There is a ThreadpoolExecutor to execute these tasks represented by the person (Consumer) * The bathroom getBathroomType() returns the current type of people occupying the bathroom. * The threadpool can switch between the 2 different queues only when the bathroom type at a given instant return null (when nobody in bathroom) * WAIT: SO a person is in wait() till the bathroom * 1. no opposition party member is there ( access when empty or only filled with his member type) * 2. till there is no room to accomodate him * EXEC CRITICAL: when a person gets to enter, * * bathroomOccupancy is incremented by 1 * setBathroomType to person.TYPE (D or R) * there is a sleep(N) call till he is in bathroom. * after he leaves he decrements the occupancy * if occupancy is 0 now, setBathroomType to null [ i missed to specify the if occupancy is 0 now, setBathroomType to null in the interview time] Verdict: Rejected."


- Design microservices and design GPS system
- Design Twitter with Notification service
- related to Unique ID generation

- topological sort and union find algorithm
- Longest common prefix for a list of words.
- https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Rubrik.csv
- https://leetcode.com/discuss/interview-question/4223585/Hard-questions-of-rubric-OA./
- https://leetcode.com/problems/delete-and-earn/description/ - Done
-   ```
    You are getting a continuous data stream of integers. You are also given a queue of size k in which you can store this integer stream. Now in this queue your task is to find the minimum absolute difference possible between 2 integers. and return it.

    For e.g
    Integer stream: 1, 2, 8, 4, 7...
    Queue size: 3
    Output: 0, 1, 1, 2, 1...
    ```
- robot bounded in circle.
- calender invite send. thread sleeping and waking using priority queue.

- Find best path in a hill with mines.
- Maximums in a sliding window - Done
- Interval intersection.
- Store a potentially large body of text which supports insert and delete operations.

- Develop sparse file system.
- Develop task runner.
- Resource allocation problems
- Design and implement a snapshot scheduler
    When designing a multithreaded scheduler, key considerations include task representation, choice of scheduling algorithm, and proper synchronization between threads. The goal is to balance workload efficiently and ensure fair task execution.

    Taking snapshots is a CPU bound task with a large turnaround time. Scheduling-wise Priority-wise queue scheduling seems like a reasonable way forward since some snapshots are more important than others. Otherwise Round-Robin seems like a wise choice. It compromises on turnaround time but ensures fairness in task execution.

- Producer-Consumer Multi-Threaded problem
- Task Scheduler with Multi-Threading
- building H2O molecule with Multi-Threading - Done
    - You use two locks and count by the number of Hydrogen atoms sent
- I had to implement thread-safe stack using a linkedlist. Push and pop should be O(1). This problem is pretty similar to Design Bounded Blocking Queue. Interviewer asked some additional questions prying into my knowledge of concurrency primitives.
- implement LRU Cache and then was asked to use threads to implement it
-   `
    I am asked the below question in Rubrik System coding just yesterday. They focus a lot on concurrency. This is asked in the first screening round. I don't think I did a good job and I likely wouldn't be considered further. This is for a senior role.

    Question
    Implement following method of ScheduledExecutorService interface in Java

    schedule(Runnable command, long delay, TimeUnit unit)
    Creates and executes a one-shot action that becomes enabled after the given delay.

    scheduleAtFixedRate(Runnable command, long initialDelay, long period, TimeUnit unit)
    Creates and executes a periodic action that becomes enabled first after the given initial delay, and subsequently with the given period; that is executions will commence after initialDelay then initialDelay+period, then initialDelay + 2 * period, and so on.

    scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)
    Creates and executes a periodic action that becomes enabled first after the given initial delay, and subsequently with the given delay between the termination of one execution and the commencement of the next.
    `



Resources:
concurrency, multithreading, mutex locks, semaphores, object oriented programing