class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] += 1
        for i,c in count.items():
            freq[c].append(i)
        result = []
        for i in range(len(freq)-1, -1, -1):
            for char in freq[i]:
                result.append(char)
                if len(result)==k:
                    return result
                    
