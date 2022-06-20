class Solution:
    '''
    def findans(self,word1,word2):
        
        l1=len(word1)
        l2=len(word2)
        i=l1-1
        j=l2-1  
        while(i>=0 and j>=0):
            if word1[i]!=word2[j]:
                return False
            i-=1
            j-=1
        return True
    '''
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        words.sort(key=len,reverse=True)
        ans=''
        for x in words:
            if x+'#' not in ans:
                ans+=x+'#'
        return len(ans)
        
        
        
        '''
        ans=''
        i=0
        while i<(len(words)-1):
            prev=words[i]
            nxt=words[i+1]
            if self.findans(prev,nxt):
                ans+=prev+'#'
                i+=1
            else:
                ans+=prev+'#'+nxt
                i+=1
        print(ans)
        '''
            
                
            
                
            
        