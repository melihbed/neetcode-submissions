class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        output_num = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    output_num *= nums[j]
            output.append(output_num)
            output_num = 1
        return output
        