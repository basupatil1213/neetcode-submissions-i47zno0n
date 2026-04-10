class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            ones = 0

            num = i
            while num:
                bit = num % 2


                num //= 2

                if bit:
                    ones += 1
            res.append(ones)
        
        return res