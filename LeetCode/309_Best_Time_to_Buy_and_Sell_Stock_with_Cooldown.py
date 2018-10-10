class Solution:

    # My thinking:
    # buy: the profit earned for sequence end with buy
    # sell: the profit earned for sequence end with sell
    # The max profit made is the end of sell sequence
    # Include cooldown: cannot buy just after sell. Thus buy[i] should compare with buy[i-1] or sell value at [i-2] deduct the current price
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[0] = 0
        sell[1] = max(0, buy[0] + prices[1])
        for i in range(2, len(prices)):
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return sell[-1]


if __name__ == "__main__":
    import random
    length = 1000
    input = [random.randint(1,100) for i in range(length)]
    solution = Solution()
    print(solution.maxProfit(input))