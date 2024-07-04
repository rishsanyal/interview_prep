import java.util.concurrent.ThreadLocalRandom;

public class Runner {

    private static final long startTime = System.currentTimeMillis();

    public static class DefaultRunnable implements Runnable {

        private TaskType type;
        private int taskId;

        DefaultRunnable(TaskType type, int taskId) {
            this.type = type;
            this.taskId = taskId;
        }

        @Override
        public void run() {
            if(this.type==TaskType.PERIODIC_NONBLOCKING) {
                try {
                    Thread.sleep(15);
                } catch(InterruptedException e) {}
            }
            System.out.printf("My task type is %s, the taskId is %d, and currentTime is %d\n",
                type.toString(), taskId, System.currentTimeMillis() - startTime);
        }
    }

    public static void main(String[] args) {
        MyScheduledExecutorService myService = new MyScheduledExecutorService();
        myService.start();

        for (int i = 0; i < 100; i++) {
            int taskType = ThreadLocalRandom.current().nextInt(3);
            if (taskType == 0) {
                myService.schedule(new DefaultRunnable(TaskType.RUN_ONCE, i+1), 500 );
            } else if(taskType==1) {
                myService.scheduleAtFixedRate(new DefaultRunnable(TaskType.PERIODIC_NONBLOCKING, i+1), 100, 300);
            } else {
                myService.scheduleWithFixedDelay(new DefaultRunnable(TaskType.PERIODIC_BLOCKING, i+1), 50, 230);
            }

        }
    }
}

==> ScheduledTask.java <==
public class ScheduledTask implements Comparable<ScheduledTask> {
    Runnable r;
    long initialRunMillis;
    long periodicDelayMillis;
    TaskType type;

    ScheduledTask(Runnable r, long initialRunMillis, long periodicDelayMillis, TaskType type) {
        this.r = r;
        this.initialRunMillis = initialRunMillis;
        this.periodicDelayMillis = periodicDelayMillis;
        this.type = type;
    }

    @Override
    public int compareTo(ScheduledTask o) {
        if(this.initialRunMillis<o.initialRunMillis) {
            return -1;
        } else if(this.initialRunMillis==o.initialRunMillis) {
            return 0;
        }
        return 1;
    }
}

==> TaskType.java <==
public enum TaskType {
    RUN_ONCE,
    PERIODIC_NONBLOCKING,
    PERIODIC_BLOCKING
}