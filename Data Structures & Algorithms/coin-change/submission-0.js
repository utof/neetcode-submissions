class Solution {
    /**
     * @param {number[]} coins
     * @param {number} amount
     * @return {number}
     */
    coinChange(coins, amount) {
        let curr_val = 0;
        let times = 0;
        for (let coin = coins.length - 1; coin >= 0; coin--) {
            while (curr_val + coins[coin] <= amount) {
                curr_val += coins[coin]
                times += 1;
            }

        }
        return curr_val === amount ? times : -1
    }
}
