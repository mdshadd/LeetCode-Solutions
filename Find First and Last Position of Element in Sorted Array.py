import bisect as b

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        output = []

        if len(nums) == 0:
            output.append(-1)
            output.append(-1)
        else:
            output = []
            i = b.bisect_left(nums, target)
            if i != len(nums) and nums[i] == target:
                output.append(i)
            else:
                output.append(-1)

            j = b.bisect_right(nums, target)
            if j != len(nums)+1 and nums[j-1] == target:
                output.append(j-1)
            else:
                output.append(-1)

        return output
