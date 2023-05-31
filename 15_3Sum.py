example = [0,0,0]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = list()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            first = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                b, c = nums[left], nums[right]
                if first + b + c == 0:
                    if [first, b, c] not in result: result.append([first, b, c])
                    right -= 1
                elif first + b + c > 0:
                    right -= 1
                else:
                    left += 1
        return result


element = Solution()
print(element.threeSum(example))
