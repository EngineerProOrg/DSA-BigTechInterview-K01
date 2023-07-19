# Heap - Live Coding Solutions

Speaker: Hiệp
## [1. Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager/description/)

```java
class SeatManager {

    // pq: unreserved seats
    PriorityQueue<Integer> pq;
    // first seat that was never reserved
    int count;
    // free seats: pq + count...n

    public SeatManager(int n) {
        pq = new PriorityQueue<>();
        count = 1;
        // free seats: 1...n
    }
    
    public int reserve() {
        if (!pq.isEmpty()) {
            // if there are unreserved seats, return the one with the smallest index
            return pq.poll();
        }
        // otherwise, return the smallest untouched seat and increase count
        return count++;
    }
    
    public void unreserve(int seatNumber) {
        // return the seat to the heap of unreserved seats
        pq.add(seatNumber);
    }
}
```

Complexity:

- Time: O(log N), where N is total number of seats.
- Space: O(N).

## [2. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // heap of k largest numbers
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int x: nums) {
            q.add(x);
            // if q exceeds k numbers, remove the smallest one
            if (q.size() > k) q.poll();
        }

        // the k-th largest number is the smallest among top-k largest numbers
        return q.poll();
    }
}
```

Complexity:

- Time: O(N * log k), where N is the length of `nums`.
- Space: O(k).

## [3. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/description/)

```java
class Solution {
    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        int[][] arr = new int[n][];
        // attach index to tasks
        for (int i = 0; i < n; ++i) {
            arr[i] = new int[]{tasks[i][0], tasks[i][1], i};
        }
        // sort tasks based on enqueue time
        Arrays.sort(arr, (task1, task2) -> task1[0] - task2[0]);

        // heap of pending tasks (pairs of {processing time, id}), prioritized by processing time and id
        PriorityQueue<int[]> pq = new PriorityQueue<>((task1, task2) -> {
            if (task1[0] != task2[0]) return task1[0] - task2[0];
            return task1[1] - task2[1];
        });
        int[] res = new int[n];
        for (int i = 0, t = 0, j = 0; i < n; ++i) {
            // if there are no tasks pending, fast forward to the next task
            if (pq.isEmpty() && arr[j][0] > t) t = arr[j][0];

            // push all new tasks until time t into the heap/queue
            while (j < n && arr[j][0] <= t) {
                pq.add(new int[]{arr[j][1], arr[j][2]});
                j++;
            }

            // get the "best" task based on the defined priority and perform the task
            var task = pq.poll();
            // update result and fast-forward until the task is complete
            res[i] = task[1];
            t += task[0];
        }
        return res;
    }
}
```

Complexity:

- Time: O(N * log N), where N is the number of tasks.
- Space: O(N).

## [4. Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/description/)

```java
class Solution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        int n = servers.length, m = tasks.length;
        // heap of free servers (pairs of {weight, id}), prioritized by server weights and id
        PriorityQueue<int[]> free = new PriorityQueue<>((server1, server2) -> {
            if (server1[0] != server2[0]) return server1[0] - server2[0];
            return server1[1] - server2[1];
        });
        // init all servers to be empty
        for (int i = 0; i < n; ++i) free.add(new int[]{servers[i], i});

        // heap of busy servers (pairs of {finish time, id}), prioritized by finish time
        PriorityQueue<long[]> busy = new PriorityQueue<>((server1, server2) -> {
            return Long.compare(server1[0], server2[0]);
        });

        int[] res = new int[m];
        // keeping track of time
        long t = 0;
        for (int i = 0; i < m; ++i) {
            // fast-forward until the next task arrives at time i
            if (i > t) t = i;
            // if there are no free servers, wait until the first busy server is done
            if (free.isEmpty() && busy.peek()[0] > t) t = busy.peek()[0];
            // move all finished server to free
            while (!busy.isEmpty() && busy.peek()[0] <= t) {
                var server = busy.poll();
                int id = (int) server[1];
                free.add(new int[]{servers[id], id});
            }

            // get the "best" server based on the priority
            var server = free.poll();
            int id = server[1];
            res[i] = id;
            // move the server to the busy heap
            busy.add(new long[]{t + tasks[i], id});
        }
        return res;
    }
}
```

Complexity:

- Time: O((N+M) * log N), where N is the number of servers, M is the number of tasks.
- Space: O(M).