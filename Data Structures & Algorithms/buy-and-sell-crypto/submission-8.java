class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int minPrice = prices[0];

        for (int p : prices) {
            minPrice = Math.min(p, minPrice);
            maxP = Math.max(p - minPrice, maxP);
        }
        return maxP;
    }
}
