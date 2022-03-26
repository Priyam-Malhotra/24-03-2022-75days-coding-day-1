class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=prices[0]
        temp=0
        for i in prices:
            ans=min(ans,i)
            temp=max(temp,i-ans)
        return temp