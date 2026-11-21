class Solution:
    def minDays(self, n: int) -> int:
        
        tri = []
        k = 1
        while k * (k+1) // 2 <= n:
            tri.append((k,k*(k+1) // 2))
            k += 1
        INF = float('inf')
        dp = [0] + [INF] * n
        for s in range(1,n+1):
            best = INF
            for kk, t in tri:
                if t > s:
                    break
                c = dp[s-t] + kk + 1
                if c <  best:
                    best = c
            dp[s] = best

        return dp[n] - 1