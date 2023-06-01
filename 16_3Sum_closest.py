example = [2,3,8,9,10]

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        nums_length = len(nums)
        result = nums[0] + nums[1] + nums[nums_length - 1]
        for i in range(nums_length - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            first = nums[i]
            left = i + 1
            right = nums_length - 1
            while left < right:
                b, c = nums[left], nums[right]
                if first + b + c == target:
                    return target
                elif first + b + c > target:
                    right -= 1
                else:
                    left += 1
                if left == right:
                    if abs(target - result) > abs(target - (first + b + c)):
                        result = first + b + c
        return result


element = Solution()
print(element.threeSumClosest(example, 16))
