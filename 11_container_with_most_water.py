class Solution:
    def maxArea(self, height) -> int:
        lidx = 0
        ridx = len(height)-1
        result = 0
        while (lidx < ridx):
            tmp = (ridx - lidx) * min(height[lidx], height[ridx])
            result = tmp if tmp > result else result
            if height[lidx] < height[ridx]: lidx += 1
            else: ridx -= 1
        return result

# BRUTE FORCE
# class Solution:
#     def maxArea(self, height) -> int:
#         result = []
#         for idx, i in enumerate(height[:-1]):
#             for jdx, j in enumerate(height[idx+1:]):
#                 result.append(min(i, j) * (jdx+1))
#         return max(result)


height = [1,8,6,2,5,4,8,3,7]
element = Solution()
print(element.maxArea(height))
