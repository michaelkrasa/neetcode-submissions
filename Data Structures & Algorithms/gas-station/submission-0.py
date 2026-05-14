class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """

        unlimited gas in tank

        cost[i] -> to the next station

        return the starting gas stations index

        gas   [ 1,2, 3,4] 
        cost  [ 2,2, 4,1]
        diff  [-1,0,-1,3]

        """

        if sum(cost) > sum(gas):
            return -1

        total = res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res

