class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        INF = 10** 9 
        dp = [INF] * (sum + 1)
        dp[0] = 0

        for num in nums:
            options = [(num,0)]

            x = num
            cost = 1
            while x // 2 > 0:
                x //= 2
                options.append((x,cost))
                cost += 1

            x = num
            cost = 1
            while x * 2 <= sum:
                x *= 2
                options.append((x,cost))
                cost += 1

            new_dp =  dp[:]

            for current in range(sum + 1):
                if dp[current] == INF:
                    continue

                for value,operations in options:
                    if current + value <= sum:
                        new_dp[current + value] = min(new_dp[current+value],dp[current] + operations)

            dp = new_dp

        return -1 if dp[sum] == INF else dp[sum]
        