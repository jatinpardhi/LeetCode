#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	count=0
    	for x in arr:
    	    if x==0:
    	        count+=1
    	i=0
    	j=0
    	while(j<len(arr)):
    	    if arr[j]!=0:
    	        arr[i]=arr[j]
    	        i+=1
    	        j+=1
    	    else:
    	        j+=1
    	while(i<len(arr)):
    	    arr[i]=0
    	    i+=1
    	return arr
    	   

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends