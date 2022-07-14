class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def ans(i,re,a):
            if i==len(nums):
                re=re.split()
                re.sort()
                if re not in a:
                    a.append(re)
                return
            ans(i+1,re+" "+str(nums[i]),a)
            ans(i+1,re,a)
            
        r=''
        aa=[]
        ans(0,r,aa)
        return aa
        