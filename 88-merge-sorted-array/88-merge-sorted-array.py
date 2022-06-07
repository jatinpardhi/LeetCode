class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        ans=len(nums1)-1
        i=m-1
        j=n-1
        
        while(j>=0):
            if i>=0 and nums1[i]>=nums2[j]:
                nums1[ans]=nums1[i]
                ans-=1
                i-=1
            else:
                nums1[ans]=nums2[j]
                ans-=1
                j-=1
                
# [1,6,9,87,90,0,0,0,0]
# [3,8,90,100]              

                
              

        