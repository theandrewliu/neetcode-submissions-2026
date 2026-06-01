class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for num in nums:
            if num in d:
                d[num] +=1
            else:
                d[num] = 1
        
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        i = 0
        while i < k:
            ans.append(list(sorted_d.keys())[i])
            i +=1
        return ans

