class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        z=nums
        nums.sort()

        res=[]
        p=lower-1
        for num in nums:
            if num<lower or num>upper:
                continue
            if num > p+1:
                res.append([p + 1,num - 1])
            p = num
        if p < upper:
            res.append([p + 1,upper])
        return res
        