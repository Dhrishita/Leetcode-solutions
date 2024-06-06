class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        
        map<int,int>d;
        
        for(int i =0 ; i<hand.size() ; i++)
        {
            d[hand[i]]++;
        }
        
        
        for(auto x= d.begin() ; x!=d.end(); )
        {
            if(x->second > 0)
            {
                for(int i = 0 ; i< groupSize ; i++)
                {
                    if(d[x->first + i] > 0)
                        d[x->first + i]--;
                    else
                        return false;
                }
            }
            else
            {
                x++;
            }
        }
        return true;
    }
};