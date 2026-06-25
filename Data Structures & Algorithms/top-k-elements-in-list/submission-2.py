class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] +=1
        for key, value in count.items():
            frequency[value].append(key)
        result = []
        for i in range(len(frequency)-1, -1, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result
        
