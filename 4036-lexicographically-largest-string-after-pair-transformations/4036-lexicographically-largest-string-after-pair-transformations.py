class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        c=nums
        ans = []
        for x in nums:
            z=x // (1<<25)
            rem = x % (1<<25)
            s=['z']*z
            for bit in range(24,-1,-1):
                if rem & (1<<bit):
                    s.append(chr(ord('a')+bit))
            ans.append(''.join(s))
        return ans
        