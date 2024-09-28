class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        candies_bool = [True] * n


        for i in range(n):
            candie = candies[i] + extraCandies
            for j in range(n):
                if (candies[j] > candie):
                    candies_bool[i] = False
                    break
        return candies_bool
