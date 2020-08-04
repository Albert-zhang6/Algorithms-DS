'''Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_nums = nums[:]
        final_nums = []
        product = 1
        
        for i in range(len(nums)):
	        new_nums.pop(i)
	        for j in new_nums:
		        product *= j
	        final_nums.insert(i,product)
	        product = 1
	        new_nums = nums[:]
            
        return final_nums