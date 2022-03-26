class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>ans;
        int i1=0;
        int i2=0;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<=nums.size();j++){
                if(nums[i+j]==target){
                    ans.push_back(i);
                    ans.push_back(j);
                    break;
                }
            }
            }
        return ans;
        }
};
