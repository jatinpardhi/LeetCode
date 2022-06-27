class Solution:
    def minPartitions(self, n: str) -> int:
        maxx=0
        for x in n:
            maxx=max(int(x),maxx)
        return maxx
            