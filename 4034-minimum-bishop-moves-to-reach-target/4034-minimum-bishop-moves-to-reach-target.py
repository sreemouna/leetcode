class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        s_r,s_c=source
        t_r,t_c = target

        if(s_r + s_c)% 2 != (t_r+t_c)% 2:
            return -1
        if abs(s_r-t_r) == abs(s_c-t_c):
            return 1
        return 2
        
        