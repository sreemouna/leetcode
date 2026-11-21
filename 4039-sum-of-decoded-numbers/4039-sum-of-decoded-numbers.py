class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0

        for num in nums:
            width = num % 10
            d = num // 10

            s = str(d)
            x = int(s[:width])
            y = int(s[width:])

            ans = (ans + pow(x,y,MOD)) % MOD

        return ans
        