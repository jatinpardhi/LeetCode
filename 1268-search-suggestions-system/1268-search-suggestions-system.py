from collections import defaultdict
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        d1=defaultdict(lambda:0)
        products.sort()
        curr=''
        for i in range(len(searchWord)):
            curr+=searchWord[i]
            d1[curr]=[]
        
        for x in products:
            cur=''
            for i in range(len(x)):
                cur+=x[i]
                if d1[cur]==0:
                    continue
                d1[cur].append(x)
        #print(d1)
        a=[]
        currr=''
        for i in range(len(searchWord)):
            currr+=searchWord[i]
            if len(d1[currr])>3:
                a.append(d1[currr][:3])
            else:
                a.append(d1[currr])
        return a
    