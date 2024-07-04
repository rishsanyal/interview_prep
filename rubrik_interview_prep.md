I am not sure of tailor-made preparation for Rubrik/Go-lang, But based on my interview experience: i have jotted down below concepts related to concurrency/multi-threading. Also note that some of these concepts might be related to Java, so please look for correspondence for go-lang.

Basic concepts:

    - Definition and differences of process/thread and relations between user threads and OS threads.
        - User level threads are created by an application and are created through the OS' API
    Causes of deadlock and avoidance of deadlocks
    Singleton design pattern [multi-level locking]
    Concurrent modification exception examples and other exceptions
    Blocking vs non-blocking io
    Async Api design
    Atomic integers and counters

Intermediate concepts:

    thread-pools and executor-service framework [java]
    synchronized vs re-entrant locks vs readwrite locks vs futures
    fork, wait and notifyAll
    Concurrent DS: implement thread-safe cache and blocking queue [producer-consumer]
    Double checked locking
    Deadlock vs live-lock
    Mutex vs Semaphores
    Dinning philosophers problem

Advance concepts:

    Concurrency design patterns [Good start point: Active object pattern]
    Map-reduce
    CPU scheduling algorithms
    Compare-and-Swap
    two-phase-locks
    Thread throttling
    Distributed Algo's and race-conditions [example rate limiter]

Please choose to study, based on level of experience. For years of experience 1-3 years basic would be sufficient.