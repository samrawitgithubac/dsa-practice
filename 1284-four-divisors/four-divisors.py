import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            divisors = set()
            for i in range(1, int(math.isqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                total += sum(divisors)
        return total