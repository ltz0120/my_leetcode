class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if len(temperatures) == 0:
            return []
        warm_temp = [0 for i in range(len(temperatures))]
        out_list = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            index = len(temperatures) - i - 1
            j = index + 1
            while (j < len(temperatures)):
                if temperatures[index] < temperatures[j]:
                    warm_temp[index] = j
                    out_list[index] = j - index
                    break
                else:
                    j = warm_temp[j]
                    if j == 0:
                        break
        return out_list

# Test
if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures(temperatures))