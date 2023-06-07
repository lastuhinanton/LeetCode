candies = [2,3,5,1,3]
extraCandies = 3

class Solution:
    def kidsWithCandies(self, candies, extra_candies):
        max_candies = max(candies)
        return [True if extra_candies + kid_candies >= max_candies else False for kid_candies in candies]

element = Solution()
element.kidsWithCandies(candies, extraCandies)
