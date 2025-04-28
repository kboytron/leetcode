class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = 0;
        int sell = 1;


        int MaxProfit = 0;
        while(sell < prices.size()){
            if(prices[buy] < prices[sell]){
                int profit = prices[sell] - prices[buy];
                if (MaxProfit < profit){
                    MaxProfit = profit;
                } 
            } else {
                buy = sell;
            }
            sell ++;
        }
        return MaxProfit;
    }
};