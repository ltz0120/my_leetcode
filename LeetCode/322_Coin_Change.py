class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        revisit = [False] * (amount + 1)
        countloop = 0
        S = []
        S.append(0)
        while S:
            temp = []
            countloop += 1
            for i in S:
                for coin in coins:
                    if i + coin == amount:
                        return countloop
                    elif i + coin < amount and not revisit[i + coin]:
                        revisit[i + coin] = True
                        temp.append(i + coin)
                S = temp

        return -1