class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        
        map<int,int>d;
        
        for(int i =0 ; i<hand.size() ; i++)
        {
            d[hand[i]]++;
        }
        
        
        for(auto m= d.begin() ; m!=d.end(); )
        {
            if(d[m->first] > 0)
            {
                for(int i = 0 ; i< groupSize ; i++)
                {
                    if(d[m->first + i] > 0)
                        d[m->first + i]--;
                    else
                        return false;
                }
            }
            else
            {
                m++;
            }
        }
        return true;
    }
};