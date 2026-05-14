class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF   # 32-bit mask
        max_int = 0x7FFFFFFF  # Max signed 32-bit int

        while b != 0:
            partial = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = partial, carry

        # if sign bit is set, interpret as negative two's complement
        return a if a <= max_int else ~(a ^ mask)
