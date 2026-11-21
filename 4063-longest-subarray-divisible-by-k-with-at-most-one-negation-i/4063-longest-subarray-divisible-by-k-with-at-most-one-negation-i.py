class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            total = 0
            seen = set()

            for j in range(i,n):
                total += nums[j]

                seen.add((2 * nums[j]) % k)

                if total % k == 0 or total % k in seen:
                    ans = max(ans,j-i+1)
                    

        return ans
        