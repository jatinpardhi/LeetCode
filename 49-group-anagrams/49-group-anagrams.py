from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1=defaultdict(lambda:[])
        for x in strs:
            xx=list(x)
            xx=sorted(xx)
            xx=''.join(xx)
            d1[xx].append(x)
        ans=[]
        for x in d1:
            ans.append(d1[x])
        return ans
            