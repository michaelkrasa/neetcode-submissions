class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count all tasks - frequency, start with the most common ones
        counter = Counter(tasks)

        maxHeap = [-c for c in counter.values()]
        heapq.heapify(maxHeap)

        # keep a queue to check whether we can process the task yet or not
        q = deque()
        
        time = 0
        while maxHeap or q:
            time += 1

            # pop task, decrement its frequency and put it into the queue
            # based on when it can be processed
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n]) # when the task can be processed
            if q and q[0][1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])

        return time



            



