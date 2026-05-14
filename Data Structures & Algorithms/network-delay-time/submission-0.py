class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # graph
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v,t))

        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            cur_dist, node = heapq.heappop(heap)

            # not an improvement
            if cur_dist > dist[node]:
                continue

            for v, t in graph[node]:
                new_dist = t + cur_dist
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        max_time = max(dist.values())
        return max_time if max_time < float('inf') else -1

        

