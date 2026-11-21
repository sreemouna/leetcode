from typing import List
import bisect
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)
        nxt = [n] * n
        stk = []

        for i in range(n-1,-1,-1):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()

            nxt[i] = stk[-1] if stk else n 
            stk.append(i)

        vals = sorted(set(nums))
        m = len(vals)

        def rank(v):
            return bisect.bisect_left(vals,v) + 1

        tree = [0] * (m+1)

        def upd(pos):
            while pos <= m :
                tree[pos] += 1
                pos += pos & (-pos)

        def qry(pos):
            s = 0
            while pos > 0:
                s += tree[pos]
                pos -= pos & (-pos)

            return s

        evts = [[] for _ in range(n)]
        for i in range(n):
            hi = nxt[i] - 1
            evts[hi].append((nums[i],1,i))
            evts[i].append((nums[i],-1,i))

        res = [0] * n
        seen = 0

        for p in range(n):
            upd(rank(nums[p]))
            seen += 1
            for v,sign,idx in evts[p]:
                gt = seen - qry(rank(v))
                res[idx] += sign * gt

        return sum(res)


        