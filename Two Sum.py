class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_of_x={}
        len_of_nums=len(nums)
        i=0
        while i<len_of_nums:
            val= target - nums[i]
            if(val in dict_of_x):
                return [dict_of_x[val],i]
            dict_of_x[nums[i]]=i
            i+=1
