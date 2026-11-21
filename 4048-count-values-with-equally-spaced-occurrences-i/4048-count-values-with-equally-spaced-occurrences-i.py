class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = {}
        for i,v in enumerate(nums):
            pos.setdefault(v,[]).append(i)
        cnt = 0
        for idxs in pos.values():
            if len(idxs) == 3 and idxs[1] - idxs[0] == idxs[2] - idxs[1]:
                cnt += 1

        return cnt
        