class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            hashmap[nums[i]] = i

        
        for i in range(0, len(nums)):
            desired_elem = target - nums[i]
            if desired_elem in hashmap and i != hashmap[desired_elem]:
                return [i, hashmap[desired_elem]]
        
