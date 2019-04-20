class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        output = [nums.index(target)]
        output.append(nums[::-1].index(target))

        if len(output) == 0:
            output.append(-1)
            output.append(-1)

        if len(output) == 1:
            output.append(output[0])

        return output
