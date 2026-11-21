class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v,[]).append(i)
        cnt = 0
        for idxs in pos.values():
            if len(idxs) < 3:
                continue

            gap = idxs[1] - idxs[0]
            if all(idxs[k] - idxs[k-1] == gap for k in range(1,len(idxs))):
                cnt += 1
        return cnt
        