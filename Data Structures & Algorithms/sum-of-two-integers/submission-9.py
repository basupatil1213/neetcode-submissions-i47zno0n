class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = a & 0xFFFFFFFF
        b = b  & 0xFFFFFFFF
        while b:
            a, b = (a ^ b), (a & b) << 1 & 0xFFFFFFFF
        return a if not a & (1 << 31) else a - 0x100000000

        