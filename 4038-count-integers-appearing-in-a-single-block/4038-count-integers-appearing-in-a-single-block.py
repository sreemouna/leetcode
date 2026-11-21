class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        blocks = [0] * 101

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                blocks[nums[i]] += 1

        ans = 0
        for count in blocks :
            if count == 1 :
                ans += 1

        return ans
        