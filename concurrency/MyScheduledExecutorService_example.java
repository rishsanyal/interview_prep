==> MyScheduledExecutorService.java <==
import java.util.PriorityQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.locks.ReentrantLock;

public class MyScheduledExecutorService {

    private final ExecutorService defaultExecutor;
    private final PriorityQueue<ScheduledTask> taskQueue = new PriorityQueue<>();
    private final ReentrantLock queueLock = new ReentrantLock();

    MyScheduledExecutorService() {
        defaultExecutor = Executors.newFixedThreadPool(100);
    }

    /**
     * Creates and executes a one-shot action that becomes enabled after the given delay.
     */
    public void schedule(Runnable command, long delayMillis) {
        queueLock.lock();
        long currentTime = System.currentTimeMillis();
        taskQueue.add(new ScheduledTask(command, currentTime + delayMillis, 0, TaskType.RUN_ONCE));
        queueLock.unlock();
    }

    /**
     * Creates and executes a periodic action that becomes enabled first after the given initial
     * delay, and subsequently with the given period; that is executions will commence after
     * initialDelay then initialDelay+period, then initialDelay + 2 * period, and so on.
     */
    public void scheduleAtFixedRate(Runnable command, long delayMillis, long periodMillis) {
        queueLock.lock();
        long currentTime = System.currentTimeMillis();
        taskQueue.add(new ScheduledTask(command, currentTime + delayMillis, periodMillis,
            TaskType.PERIODIC_NONBLOCKING));
        queueLock.unlock();
    }

    /**
     * Creates and executes a periodic action that becomes enabled first after the given initial
     * delay, and subsequently with the given delay between the termination of one execution and the
     * commencement of the next.
     */
    public void scheduleWithFixedDelay(Runnable command, long delayMillis, long periodMillis) {
        queueLock.lock();
        long currentTime = System.currentTimeMillis();
        taskQueue.add(
            new ScheduledTask(command, currentTime + delayMillis, periodMillis,
                TaskType.PERIODIC_BLOCKING));
        queueLock.unlock();
    }

    public void start() {
        defaultExecutor.submit(() -> {
            for (; ; ) {
                queueLock.lock();
                long currentTime = System.currentTimeMillis();
                if (taskQueue.isEmpty() || taskQueue.peek().initialRunMillis > currentTime) {
                    queueLock.unlock();
                    try {
                        Thread.sleep(1);
                    } catch (InterruptedException e) {
                    }
                    continue;
                }
                ScheduledTask currentTask = taskQueue.poll();

                switch (currentTask.type) {
                    case RUN_ONCE:
                        defaultExecutor.submit(currentTask.r);
                        break;
                    case PERIODIC_NONBLOCKING:
                        defaultExecutor.submit(currentTask.r);
                        taskQueue.add(new ScheduledTask(currentTask.r,
                            currentTime + currentTask.periodicDelayMillis,
                            currentTask.periodicDelayMillis,
                            TaskType.PERIODIC_NONBLOCKING));
                        break;
                    case PERIODIC_BLOCKING:
                        defaultExecutor.submit(() -> {
                            Future p = defaultExecutor.submit(currentTask.r);
                            try {
                                p.get();
                            } catch (Exception e) {
                                e.printStackTrace();
                            }
                            long thenTime = System.currentTimeMillis();
                            taskQueue.add(new ScheduledTask(currentTask.r,
                                thenTime + currentTask.periodicDelayMillis,
                                currentTask.periodicDelayMillis,
                                TaskType.PERIODIC_BLOCKING));
                        });
                }
                queueLock.unlock();
            }
        });
    }
}