class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
       vector<int> ans;
        int temp=1;
        for(int i=digits.size()-1;i>=0;i--){
            int val=(digits[i]+temp)%10;
            ans.push_back(val);
            temp=(digits[i]+temp)/10;
        }
        if(temp==1)
            ans.push_back(1);
        reverse(ans.begin(),ans.end());
        return ans;
    }
};