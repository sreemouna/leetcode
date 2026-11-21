class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n=len(nums)
        m=nums
        def fact(x):
            fact=set()
            d=2
            while d*d<=x:
                if x % d==0:
                    fact.add(d)
                    while x % d==0:
                        x//=d
                d += 1
            if x>1:
                fact.add(x)
            return fact
        fact=[fact(x) for x in nums]

        count={}
        distinct=0
        left=0
        ans=0
        for right in range(n):
            for p in fact[right]:
                if count.get(p,0)==0:
                    distinct += 1
                count[p]=count.get(p,0)+ 1
            while distinct > k:
                for p in fact[left]:
                    count[p] -= 1

                    if count[p]==0:
                        distinct -= 1
                        del count[p]
                left += 1
            ans = max(ans,right-left+1)
        return ans
        