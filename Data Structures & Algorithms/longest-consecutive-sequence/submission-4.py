class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        lengthCounter = []

        counter = 0
        if len(nums) == 0:
            return counter
        
        sorted_nums = sorted(set(nums)) # [-1, 0, 1, 3, 4, 5, 6, 7, 8 ,9]

        counter = 1
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i+1] == sorted_nums[i] + 1:
                counter += 1
            else:
                lengthCounter.append(counter)
                counter = 1

        if counter not in lengthCounter:
            lengthCounter.append(counter)

        #if len(lengthCounter) == 0:
        #    lengthCounter.append(counter)

        return max(lengthCounter)
                