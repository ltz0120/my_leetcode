class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        values = [1 for i in range(len(ratings))]
        visit = [False for i in range(len(ratings))]
        values = [0] + values + [0]
        ratings = [10000] + ratings + [10000]
        visit = [False] + visit + [False]

        for i in range(1, len(ratings) - 1):
            if not visit[i]:
                if ratings[i] <= ratings[i - 1] and ratings[i] <= ratings[i + 1]:
                    values[i] = 1
                    visit[i] = True
                elif ratings[i] > ratings[i - 1] and ratings[i] <= ratings[i + 1]:
                    values[i] = 1 + self.helper(ratings, values, visit, i - 1, 0)
                    visit[i] = True
                elif ratings[i] <= ratings[i - 1] and ratings[i] > ratings[i + 1]:
                    values[i] = 1 + self.helper(ratings, values, visit, 0, i + 1)
                    visit[i] = True
                elif ratings[i] > ratings[i - 1] and ratings[i] > ratings[i + 1]:
                    values[i] = 1 + self.helper(ratings, values, visit, i - 1, i + 1)
                    visit[i] = True

    def helper(self, ratings, values,visit, left, right):
        if left == 0:
            if ratings[right] <= ratings[right + 1]:
                visit[right] = True
                return 1
            else:
                if visit[right]:
                    return values[right]
                else:
                    visit[right] = True
                    return self.helper(ratings, values, 0, right + 1)
        elif right == 0:
            if ratings[left] <= ratings[left - 1]:
                visit[left] = True
                return 1
            else:
                if visit[left]:
                    return values[left]
                else:
                    visit[left] = True
                    return self.helper(ratings, values, left - 1, 0)
        else:
            if values[left] <= values[left - 1]:
                visit[left] = True