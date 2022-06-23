class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        #initlize the heap
        heap = []
        #sort the courses by end time
        courses.sort(key = lambda x: x[-1])
        #define the variable for current time
        cur = 0
        #traverse all the courses to build the heap
        for time, end in courses:
            cur += time
            #add negative value to min heap
            heapq.heappush(heap, -time)
            #delete longest task if current time is not enough
            if cur > end:
                cur += heapq.heappop(heap)
        return len(heap)
                
                
            
            
            
            
            
            
        