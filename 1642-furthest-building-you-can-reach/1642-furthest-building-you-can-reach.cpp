class Solution {
public:
     int furthestBuilding(vector<int>& v, int b, int l) 
     {
        priority_queue<int> q;
        int i;
        for(i = 0; i < v.size()-1; i++)
        {
            int d = v[i+1]-v[i];
            if(d <= 0) continue;
            if(d <= b)
            {
                b -= d;
                q.push(d);
            }
            else if(l > 0)
            {
                if(!q.empty() and d < q.top())
                {
                    b += q.top();
                    q.pop();
                    b -= d;
                    q.push(d);
                }
                l--;
            }
            else break;
        }
        return i;
     }
};
    
    
    
    