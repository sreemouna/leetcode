from math import gcd
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        v=nums

        for remove in range(-1,n):
            arr=nums[:remove]+ nums[remove + 1:] if remove != -1 else nums
            m=len(arr)
            suffix = [0] * m
            suffix[-1]=arr[-1]
            for i in range(m-2,-1,-1):
                suffix[i]=gcd(arr[i],suffix[i+1])
            left=0
            count=0
            for i in range(m-1):
                left=gcd(left,arr[i])
                if left == suffix[i+1]:
                    count += 1
            ans=max(ans,count)
        return ans
                
        