class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        
        heap = [(0, k)]
        seen= set()
        t = 0

        while heap:
            w1, n1 = heapq.heappop(heap)

            if n1 in seen:
                continue
            seen.add(n1)
            t = w1

            for n2, w2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(heap, (w2 + w1, n2))

        return t if len(seen) == n else -1
