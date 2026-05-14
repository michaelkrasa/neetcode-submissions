class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = Counter(tasks)
        

        # max heap
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)
        
        cooldown = deque() # time, count
        time = 0

        while cooldown or heap:
            time += 1

            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])

            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count != 0:
                    cooldown.append((time + n + 1, count))

        return time


            

