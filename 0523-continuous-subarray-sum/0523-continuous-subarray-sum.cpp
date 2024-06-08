class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
      unordered_map<int,int>d;
      d[0] = 0;
      int sum = 0;
      for(int i=0;i<nums.size();i++)
      {
          sum+=nums[i];
          if(d.find(sum%k) == d.end())
          {
              d[sum%k] = i+1;
          }
          else if(d[sum%k]<i)
          {
              return true;
          }
      }
        return false;
    }
};