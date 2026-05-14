class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dest = edges[i]
            adj[src].append((dest, succProb[i]))
            adj[dest].append((src, succProb[i]))

        heap = [(1, start_node)]
        seen = set()
        
        while heap:
            prob, cur = heapq.heappop_max(heap)
            seen.add(cur)

            if cur == end_node:
                return prob

            for nei, edgeProb in adj[cur]:
                if nei not in seen:
                    heapq.heappush_max(heap, (edgeProb * prob, nei))

        return 0.0
