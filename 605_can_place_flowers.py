flowerbed = [1,0,0,0,1]
n = 2

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        index = 0
        length = len(flowerbed)
        while index < length and count < n:
            if flowerbed[index] == 1: index += 2
            else:
                if index == length - 1:
                    count += 1
                    index += 1
                else:
                    if flowerbed[index + 1]: index += 3
                    else:
                        count += 1
                        index += 2
        return True if count == n else False

element = Solution()
print(element.canPlaceFlowers(flowerbed, n))