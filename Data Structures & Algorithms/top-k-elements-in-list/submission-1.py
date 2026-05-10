class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        l = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        for i, key in enumerate(list(sorted_dict.keys())[:k]):
            l.append(key)
        
        return l
